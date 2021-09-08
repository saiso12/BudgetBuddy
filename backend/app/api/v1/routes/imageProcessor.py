from fastapi import APIRouter, File, UploadFile
from typing import List
import time
import asyncio
import logging
from app.controllers.imageProcessor import read_image
from app.helpers.utils import _save_file_to_server


router = APIRouter()

log = logging.getLogger("imageProcessor")

@router.post("/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        log.info("Images Uploaded: ", img.filename)
        temp_file = _save_file_to_server(img, path="./", save_as=img.filename)
        tasks.append(asyncio.create_task(read_image(temp_file)))
    text = await asyncio.gather(*tasks)
    for i in range(len(text)):
        response[Images[i].filename] = text[i]
    response["Time Taken"] = round((time.time() - s),2)
    return response