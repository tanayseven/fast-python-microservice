from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index_endpoint() -> dict:
    return {"msg": "Hey"}
