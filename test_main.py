import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns correct status"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    assert "message" in data


def test_health_endpoint():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "FastAPI"
    assert "timestamp" in data


def test_status_endpoint():
    """Test the status check endpoint"""
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    assert data["service"] == "FastAPI Health Check Service"
    assert "timestamp" in data
    assert "uptime" in data
    # Check that uptime is a valid format (contains time units)
    assert any(unit in data["uptime"] for unit in ["s", "m", "h", "d"])
