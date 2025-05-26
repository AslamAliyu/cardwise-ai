from fastapi import APIRouter, File, UploadFile
from app.services.ocr import extract_text_from_image

router = APIRouter(prefix="/receipts", tags=["Receipts"])

@router.post("/upload")
async def upload_receipt(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_image(contents)
    return {"extracted_text": text}

