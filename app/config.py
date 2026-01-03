import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "FastAPI App")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", 2))
print("DEBUG APP_NAME =", APP_NAME)
