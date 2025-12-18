from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.pdf_extractor import extract_sections
# from app.translator import translate_section
from app.translator import translate_batch

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/extract")
async def extract(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return extract_sections(file_path)

@router.post("/translate")
async def translate(data: dict):
    sections = data.get("sections", [])
    return translate_batch(sections)
