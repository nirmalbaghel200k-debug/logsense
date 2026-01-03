from app.logger import logger
from app.config import MAX_UPLOAD_MB
from fastapi import APIRouter, UploadFile, File, HTTPException
import json

from app.db import SessionLocal
from app.models.log import Log
from app.services.log_parser import detect_severity

# ✅ router MUST be defined before using decorators
router = APIRouter()

MAX_SIZE = MAX_UPLOAD_MB * 1024 * 1024



# -------------------------
# UPLOAD LOG
# -------------------------
@router.post("/logs/upload")
async def upload_log(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="File too large (max 2MB)")

    text = content.decode("utf-8", errors="ignore")

    try:
        json.loads(text)
        format_type = "json"
    except:
        format_type = "plain_text"

    severity = detect_severity(text)

    db = SessionLocal()
    try:
        log = Log(
            filename=file.filename,
            format=format_type,
            severity=severity,
            content=text
        )
        db.add(log)
        db.commit()
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()

    return {
        "status": "saved",
        "severity": severity
    }


# -------------------------
# SEARCH LOGS (PAGINATION)
# -------------------------
@router.get("/logs/search")
def search_logs(format: str, limit: int = 10, offset: int = 0):
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=400, detail="limit must be 1–100")
    if offset < 0:
        raise HTTPException(status_code=400, detail="offset must be >= 0")

    db = SessionLocal()
    total = db.query(Log).filter(Log.format == format).count()

    logs = (
        db.query(Log)
        .filter(Log.format == format)
        .offset(offset)
        .limit(limit)
        .all()
    )
    db.close()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": [
            {
                "id": l.id,
                "filename": l.filename,
                "severity": l.severity
            }
            for l in logs
        ]
    }


# -------------------------
# LOG STATS
# -------------------------
@router.get("/logs/stats")
def log_stats():
    db = SessionLocal()
    stats = {
        "ERROR": db.query(Log).filter(Log.severity == "ERROR").count(),
        "WARNING": db.query(Log).filter(Log.severity == "WARNING").count(),
        "INFO": db.query(Log).filter(Log.severity == "INFO").count()
    }
    db.close()
    return stats
