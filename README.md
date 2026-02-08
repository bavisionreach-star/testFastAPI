# testFastAPI

This is a simple FastAPI application with health and status check endpoints.

## Features

- **Health Check Endpoint** (`/health`): Returns the health status of the application
- **Status Endpoint** (`/status`): Returns whether the service is running
- **Root Endpoint** (`/`): Welcome message

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Response**: Welcome message with status

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Response**: JSON with health status, service name, and timestamp

### Status Check
- **URL**: `/status`
- **Method**: `GET`
- **Response**: JSON with running status, service name, timestamp, and uptime info

## Testing the Endpoints

You can test the endpoints using curl or your browser:

```bash
# Root endpoint
curl http://127.0.0.1:8000/

# Health check
curl http://127.0.0.1:8000/health

# Status check
curl http://127.0.0.1:8000/status
```

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
