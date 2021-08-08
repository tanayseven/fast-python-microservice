from fastapi import FastAPI

from src.users.http_endpoints import router as users_router
from src.file_management.http_endpoints import router as file_management_router
from src.create_job.http_endpoints import router as create_job_router

app = FastAPI()

app.include_router(users_router)
app.include_router(file_management_router)
app.include_router(create_job_router)


@app.get("/")
async def index_endpoint() -> dict:
    return {"msg": "Hey"}
