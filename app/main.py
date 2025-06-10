from fastapi import FastAPI
from app.routers import tasks
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/", redirect_slashes=True)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def health_check():
    return {"status": "API Online"}
