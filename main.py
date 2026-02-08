from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime, UTC

app = FastAPI(title="Simple FastAPI Health Check", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI Health Check Service",
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
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "running",
            "service": "FastAPI Health Check Service",
            "timestamp": datetime.now(UTC).isoformat(),
            "uptime": "Service is operational"
        }
    )
