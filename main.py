from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title="Server Time API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Server Time API", "docs": "/docs"}


@app.get("/time")
def get_server_time():
    now = datetime.now(timezone.utc)
    return {
        "utc": now.isoformat(),
        "unix": int(now.timestamp()),
        "timezone": "UTC",
    }
