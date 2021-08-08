from typing import Optional

from fastapi import APIRouter, File, UploadFile
from fastapi.logger import logger

router = APIRouter()


@router.post("/file/upload", tags=["file", "upload"])
async def file_upload(file: UploadFile = File(...)) -> dict:
    content = await file.read()
    text_content: Optional[str] = None
    if isinstance(content, bytes):
        text_content = content.decode(encoding="utf-8")
    logger.info(f"{text_content}")
    return {"message": f"{file.filename} successfully uploaded"}
