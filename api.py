import shutil
from fastapi import APIRouter, UploadFile


video_router = APIRouter()


@video_router.post("/file")
async def upload_file(file: UploadFile):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}


@video_router.post("/files")
async def upload_files(files: list[UploadFile]):
    for file in files:
        with open(file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

    return {"file_name": 'fine'}
