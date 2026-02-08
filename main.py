from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime, UTC
import time

app = FastAPI(title="Simple FastAPI Health Check", version="1.0.0")

# Track application start time
APP_START_TIME = time.time()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Hello Rushi! Welcome to FastAPI Health Check Service!",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint - returns the current health status of the application"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "healthy",
            "service": "FastAPI",
            "timestamp": datetime.now(UTC).isoformat()
        }
    )


@app.get("/status")
async def status_check():
    """Status endpoint - returns whether the service is running"""
    uptime_seconds = int(time.time() - APP_START_TIME)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    
    # Format uptime string
    if uptime_days > 0:
        uptime_str = f"{uptime_days}d {uptime_hours % 24}h {uptime_minutes % 60}m"
    elif uptime_hours > 0:
        uptime_str = f"{uptime_hours}h {uptime_minutes % 60}m"
    elif uptime_minutes > 0:
        uptime_str = f"{uptime_minutes}m {uptime_seconds % 60}s"
    else:
        uptime_str = f"{uptime_seconds}s"
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "running",
            "service": "FastAPI Health Check Service",
            "timestamp": datetime.now(UTC).isoformat(),
            "uptime": uptime_str
        }
    )
