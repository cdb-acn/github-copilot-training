from typing import Dict, List
import asyncio
from fastapi import FastAPI, HTTPException

from app.models import TaskStatus, DeveloperTask, ProductivityReport, TaskCompletionMetrics


# --- Mock Database / In-Memory Service Logic
MOCK_TASKS: Dict[int, DeveloperTask] = {
    1: DeveloperTask(task_id=1, title="Refactor legacy service", status=TaskStatus.COMPLETE, hours_spent=8.5),
    2: DeveloperTask(task_id=2, title="Implement new user auth flow", status=TaskStatus.IN_PROGRESS, hours_spent=15.0),
    3: DeveloperTask(task_id=3, title="Write unit tests for checkout", status=TaskStatus.PENDING, hours_spent=0.0),
}

# Simulate asynchronous I/O with a slight delay
async def fetch_all_tasks() -> List[DeveloperTask]:
    """Simulates fetching all tasks asynchronously."""
    await asyncio.sleep(0.01)
    return list(MOCK_TASKS.values())

async def generate_productivity_report() -> ProductivityReport:
    """Builds a productivity summary from all currently stored tasks."""
    tasks = await fetch_all_tasks()
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.status == TaskStatus.COMPLETE)
    
    total_hours_spent = sum(task.hours_spent for task in tasks)
    completion_rate = round(completed_tasks / total_tasks, 2) if total_tasks > 0 else 0.0
    
    return ProductivityReport(
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        total_hours_spent=round(total_hours_spent, 2),
        completion_rate=completion_rate
    )


# --- FastAPI Initialization and Routes ---
app = FastAPI(title="Productivity Reporting System")

@app.get("/status")
async def get_status() -> Dict[str, str]:
    """Health-check endpoint used to confirm the API is running."""
    return {"status": "ok"}


@app.get("/tasks", response_model=List[DeveloperTask])
async def get_all_tasks() -> List[DeveloperTask]:
    """Returns a list of all logged tasks."""
    return await fetch_all_tasks()


@app.get("/report", response_model=ProductivityReport)
async def get_productivity_report() -> ProductivityReport:
    """Returns the calculated productivity report."""
    return await generate_productivity_report()


@app.post("/log_task")
async def log_task(task: DeveloperTask) -> TaskCompletionMetrics:
    """Stores a task and returns aggregate task-completion metrics."""
    new_id = max(MOCK_TASKS.keys()) + 1 if MOCK_TASKS else 1
    task.task_id = new_id
    MOCK_TASKS[new_id] = task
    
    # Calculate task completion metrics
    tasks = list(MOCK_TASKS.values())
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.status == TaskStatus.COMPLETE)
    pending_tasks = sum(1 for t in tasks if t.status == TaskStatus.PENDING)
    in_progress_tasks = sum(1 for t in tasks if t.status == TaskStatus.IN_PROGRESS)
    
    return TaskCompletionMetrics(
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        in_progress_tasks=in_progress_tasks
    )

@app.get("/task/{task_id}/status", response_model=TaskStatus)
async def get_task_status(task_id: int) -> TaskStatus:
    """Returns the status for a task id, or 404 when the task does not exist."""
    task = MOCK_TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.status  