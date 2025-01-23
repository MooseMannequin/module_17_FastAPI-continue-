from fastapi import FastAPI
from .routers import task, user

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)


'''
КОМАНДА

python -m uvicorn app.main:app

ИЗ ПРОЕКТА ДЛЯ ЗАПУСКА FastAPI'''
