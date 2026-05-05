from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API работает"}

@app.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "Первая задача"}]