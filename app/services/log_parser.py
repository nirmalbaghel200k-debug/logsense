# app/services/log_parser.py

"""
This file is responsible for:
- Keeping in-memory storage of logs
- (Later) parsing, severity detection, stats etc.
For now: ONLY storage. Simple and stable.
"""

# -------------------------------
# In-memory log storage
# -------------------------------
LOG_STORE = {
    "json": [],
    "plain_text": []
}


# -------------------------------
# Helper functions (optional, future-safe)
# -------------------------------

def add_log(format_type: str, filename: str, content: str):
    """
    Add a log entry to the store.
    """
    if format_type not in LOG_STORE:
        raise ValueError("Invalid log format")

    LOG_STORE[format_type].append({
        "filename": filename,
        "content": content
    })


def get_logs(format_type: str):
    """
    Get logs by format.
    """
    if format_type not in LOG_STORE:
        raise ValueError("Invalid log format")

    return LOG_STORE[format_type]


def clear_logs():
    """
    Clear all logs (useful for testing).
    """
    for key in LOG_STORE:
        LOG_STORE[key].clear()
def detect_severity(text: str) -> str:
    text = text.lower()

    if "error" in text or "failed" in text or "exception" in text:
        return "ERROR"
    elif "warning" in text or "warn" in text:
        return "WARNING"
    else:
        return "INFO"
