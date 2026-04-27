"""Unit tests for main.py utility functions."""

import pytest
from fastapi import HTTPException

from app.main import (
    MOCK_TASKS,
    fetch_all_tasks,
    generate_productivity_report,
    get_task_status,
    log_task,
)
from app.models import DeveloperTask, TaskStatus, ProductivityReport


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_list_of_tasks() -> None:
    """Test that fetch_all_tasks returns all tasks from MOCK_TASKS."""
    tasks = await fetch_all_tasks()
    assert isinstance(tasks, list)
    assert len(tasks) > 0
    assert all(isinstance(task, DeveloperTask) for task in tasks)


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_correct_count() -> None:
    """Test that fetch_all_tasks returns the correct number of tasks."""
    tasks = await fetch_all_tasks()
    assert len(tasks) == len(MOCK_TASKS)


@pytest.mark.asyncio
async def test_generate_productivity_report_returns_valid_metrics() -> None:
    """Test that generate_productivity_report returns a valid ProductivityReport."""
    report = await generate_productivity_report()
    assert isinstance(report, ProductivityReport)
    assert report.total_tasks > 0
    assert report.completed_tasks >= 0
    assert 0.0 <= report.completion_rate <= 1.0
    assert report.total_hours_spent >= 0.0


@pytest.mark.asyncio
async def test_generate_productivity_report_calculates_completion_rate() -> None:
    """Test that generate_productivity_report calculates completion_rate correctly."""
    report = await generate_productivity_report()
    expected_rate = round(report.completed_tasks / report.total_tasks, 2) if report.total_tasks > 0 else 0.0
    assert report.completion_rate == expected_rate


@pytest.mark.asyncio
async def test_generate_productivity_report_sums_hours_spent() -> None:
    """Test that generate_productivity_report correctly sums hours_spent."""
    tasks = await fetch_all_tasks()
    expected_hours = sum(task.hours_spent for task in tasks)
    report = await generate_productivity_report()
    assert report.total_hours_spent == round(expected_hours, 2)


@pytest.mark.asyncio
async def test_generate_productivity_report_returns_zero_rate_when_no_tasks() -> None:
    """Test completion_rate is 0.0 when there are no tasks."""
    MOCK_TASKS.clear()

    report = await generate_productivity_report()

    assert report.total_tasks == 0
    assert report.completed_tasks == 0
    assert report.total_hours_spent == 0.0
    assert report.completion_rate == 0.0


@pytest.mark.asyncio
async def test_log_task_assigns_new_id_and_returns_expected_metrics() -> None:
    """Test log_task rewrites task_id and returns exact metrics."""
    task = DeveloperTask(
        task_id=999,
        title="Unit test task",
        status=TaskStatus.IN_PROGRESS,
        hours_spent=1.25,
    )
    expected_new_id = max(MOCK_TASKS.keys()) + 1

    metrics = await log_task(task)

    assert task.task_id == expected_new_id
    assert expected_new_id in MOCK_TASKS
    assert metrics.total_tasks == len(MOCK_TASKS)
    assert metrics.completed_tasks == sum(1 for t in MOCK_TASKS.values() if t.status == TaskStatus.COMPLETE)
    assert metrics.pending_tasks == sum(1 for t in MOCK_TASKS.values() if t.status == TaskStatus.PENDING)
    assert metrics.in_progress_tasks == sum(1 for t in MOCK_TASKS.values() if t.status == TaskStatus.IN_PROGRESS)


@pytest.mark.asyncio
async def test_log_task_uses_id_one_when_store_is_empty() -> None:
    """Test log_task starts IDs at 1 when no tasks exist."""
    MOCK_TASKS.clear()
    task = DeveloperTask(
        task_id=42,
        title="First task",
        status=TaskStatus.PENDING,
        hours_spent=0.0,
    )

    metrics = await log_task(task)

    assert task.task_id == 1
    assert 1 in MOCK_TASKS
    assert metrics.total_tasks == 1
    assert metrics.pending_tasks == 1


@pytest.mark.asyncio
async def test_get_task_status_returns_existing_status() -> None:
    """Test get_task_status returns status payload for existing task."""
    result = await get_task_status(1)
    assert result == {"status": TaskStatus.COMPLETE}


@pytest.mark.asyncio
async def test_get_task_status_raises_404_for_missing_task() -> None:
    """Test get_task_status raises HTTPException for missing tasks."""
    with pytest.raises(HTTPException) as exc_info:
        await get_task_status(999_999)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task not found"
