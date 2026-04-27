"""Integration tests for FastAPI endpoints."""

import pytest
from httpx import AsyncClient

from app.models import DeveloperTask, TaskStatus, ProductivityReport, TaskCompletionMetrics


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_endpoint_returns_ok(client: AsyncClient) -> None:
    """Test that GET /status returns status ok."""
    response = await client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_all_tasks_returns_list(client: AsyncClient) -> None:
    """Test that GET /tasks returns a list of tasks."""
    response = await client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_all_tasks_returns_developer_tasks(client: AsyncClient) -> None:
    """Test that GET /tasks returns valid DeveloperTask objects."""
    response = await client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    for task in data:
        assert "task_id" in task
        assert "title" in task
        assert "status" in task
        assert "hours_spent" in task
        assert task["status"] in ["pending", "in_progress", "complete"]


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_productivity_report_returns_valid_report(client: AsyncClient) -> None:
    """Test that GET /report returns a valid ProductivityReport."""
    response = await client.get("/report")
    assert response.status_code == 200
    data = response.json()
    assert "total_tasks" in data
    assert "completed_tasks" in data
    assert "total_hours_spent" in data
    assert "completion_rate" in data
    assert isinstance(data["total_tasks"], int)
    assert isinstance(data["completed_tasks"], int)
    assert isinstance(data["total_hours_spent"], (int, float))
    assert isinstance(data["completion_rate"], (int, float))


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_creates_and_returns_metrics(client: AsyncClient) -> None:
    """Test that POST /log_task creates a task and returns TaskCompletionMetrics."""
    task_data = {
        "task_id": 999,
        "title": "Test Task",
        "status": "pending",
        "hours_spent": 2.5
    }
    response = await client.post("/log_task", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert "total_tasks" in data
    assert "completed_tasks" in data
    assert "pending_tasks" in data
    assert "in_progress_tasks" in data
    assert data["total_tasks"] > 0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_increments_total_tasks(client: AsyncClient) -> None:
    """Test that logging a task increments the total task count."""
    # Get current total
    response = await client.get("/report")
    initial_total = response.json()["total_tasks"]
    
    # Log a new task
    task_data = {
        "task_id": 998,
        "title": "Another Test Task",
        "status": "in_progress",
        "hours_spent": 1.0
    }
    response = await client.post("/log_task", json=task_data)
    
    # Verify task count increased
    assert response.status_code == 200
    data = response.json()
    assert data["total_tasks"] == initial_total + 1


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_with_complete_status(client: AsyncClient) -> None:
    """Test logging a completed task updates completed_tasks count."""
    # Get current completed count
    response = await client.get("/report")
    initial_completed = response.json()["completed_tasks"]
    
    # Log a completed task
    task_data = {
        "task_id": 997,
        "title": "Completed Task",
        "status": "complete",
        "hours_spent": 5.0
    }
    response = await client.post("/log_task", json=task_data)
    
    # Verify completed count increased
    assert response.status_code == 200
    data = response.json()
    assert data["completed_tasks"] == initial_completed + 1


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_task_status_returns_status_for_existing_task(client: AsyncClient) -> None:
    """Test that GET /task/{task_id}/status returns the task status for an existing task."""
    task_data = {
        "task_id": 996,
        "title": "Status Endpoint Test Task",
        "status": "complete",
        "hours_spent": 3.0,
    }
    create_response = await client.post("/log_task", json=task_data)
    assert create_response.status_code == 200

    tasks_response = await client.get("/tasks")
    assert tasks_response.status_code == 200
    created_task = next(task for task in tasks_response.json() if task["title"] == task_data["title"])

    response = await client.get(f"/task/{created_task['task_id']}/status")
    assert response.status_code == 200
    assert response.json() == {"status": task_data["status"]}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_task_status_returns_404_for_missing_task(client: AsyncClient) -> None:
    """Test that GET /task/{task_id}/status returns 404 when task is missing."""
    response = await client.get("/task/999999/status")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_invalid_status(client: AsyncClient) -> None:
    """Test POST /log_task returns 422 for invalid enum value."""
    response = await client.post(
        "/log_task",
        json={
            "task_id": 10,
            "title": "Invalid status task",
            "status": "done",
            "hours_spent": 1.0,
        },
    )
    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_missing_required_fields(client: AsyncClient) -> None:
    """Test POST /log_task returns 422 when title is missing."""
    response = await client.post(
        "/log_task",
        json={
            "task_id": 11,
            "status": "pending",
            "hours_spent": 1.0,
        },
    )
    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_rejects_invalid_hours_type(client: AsyncClient) -> None:
    """Test POST /log_task returns 422 when hours_spent has invalid type."""
    response = await client.post(
        "/log_task",
        json={
            "task_id": 12,
            "title": "Invalid hours",
            "status": "pending",
            "hours_spent": "two hours",
        },
    )
    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_task_status_rejects_non_integer_task_id(client: AsyncClient) -> None:
    """Test GET /task/{task_id}/status returns 422 for non-integer task_id."""
    response = await client.get("/task/not-a-number/status")
    assert response.status_code == 422
