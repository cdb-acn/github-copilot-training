"""Unit tests for main.py utility functions."""

import pytest

from app.main import MOCK_TASKS, fetch_all_tasks, generate_productivity_report
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
