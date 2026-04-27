"""Shared fixtures for tests."""

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.main import app, MOCK_TASKS


INITIAL_TASKS = {
    task_id: task.model_copy(deep=True)
    for task_id, task in MOCK_TASKS.items()
}


@pytest.fixture(autouse=True)
def reset_mock_tasks() -> None:
    """Reset in-memory task store for deterministic tests."""
    MOCK_TASKS.clear()
    MOCK_TASKS.update(
        {
            task_id: task.model_copy(deep=True)
            for task_id, task in INITIAL_TASKS.items()
        }
    )


@pytest_asyncio.fixture
async def client() -> AsyncClient:
    """Provides an async HTTP client for testing endpoints."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def app_fixture() -> FastAPI:
    """Provides the FastAPI application instance."""
    return app
