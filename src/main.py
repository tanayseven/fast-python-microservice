from fastapi import FastAPI

from src.users.http_endpoints import router as users_routers

app = FastAPI()

app.include_router(users_routers)


@app.get("/")
async def index_endpoint() -> dict:
    return {"msg": "Hey"}
