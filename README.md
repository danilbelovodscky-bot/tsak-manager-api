from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# модель задачи
class Task(BaseModel):
    title: str
    completed: bool = False

# "база данных" (пока просто список)
tasks = []
task_id_counter = 1

# 🔹 GET /
@app.get("/")
def root():
    return {"message": "API работает"}

# 🔹 GET /tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# 🔹 POST /tasks (создание задачи)
"/tasks"
def create_task(task: Task):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task

# 🔹 DELETE /tasks/{task_id}
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Задача удалена"}

    raise HTTPException(status_code=404, detail="Задача не найдена")