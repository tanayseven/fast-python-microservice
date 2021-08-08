from fastapi import FastAPI

from src.users.http_endpoints import router as users_routers
from src.file_management.http_endpoints import router as file_management_routers

app = FastAPI()

app.include_router(users_routers)
app.include_router(file_management_routers)


@app.get("/")
async def index_endpoint() -> dict:
    return {"msg": "Hey"}
