from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(
    title="LogSense",
    version="0.1.0",
    description="Log analysis API with web UI"
)

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# ---------------- STATIC ----------------
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# ---------------- ROOT UI ----------------
@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# ---------------- API ----------------
@app.post("/analyze", tags=["Log Analysis"])
async def analyze_logs(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    content = await file.read()
    lines = content.decode(errors="ignore").splitlines()

    errors, warnings, critical = [], [], []

    for line in lines:
        l = line.lower()
        if "critical" in l:
            critical.append(line)
        elif "error" in l:
            errors.append(line)
        elif "warn" in l:
            warnings.append(line)

    return {
        "summary": {
            "total_lines": len(lines),
            "errors": len(errors),
            "warnings": len(warnings),
            "critical": len(critical)
        },
        "top_errors": [
            {
                "message": msg,
                "count": errors.count(msg),
                "severity": "ERROR"
            }
            for msg in set(errors)
        ]
    }
