from fastapi import APIRouter

router = APIRouter()


@router.post("/user/login", tags=["users", "login"])
async def user_login() -> dict:
    return {"message": "login successful"}


@router.post("/user/sign-up", tags=["users", "sign-up"])
async def user_sign_up() -> dict:
    return {"message": "sign up successful"}
