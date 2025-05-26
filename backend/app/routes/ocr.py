from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.ocr import extract_text

router = APIRouter()

@router.post("/ocr")
async def ocr_route(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text(temp_path)
    finally:
        os.remove(temp_path)

    return {"extracted_text": text}

