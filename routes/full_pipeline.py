from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from modules.full_pipeline import FullPipeline
import cv2
import json
import io
from PIL import Image 
import numpy as np 

router = APIRouter()

async def read_image(file: UploadFile=File(...)):
    try:
        img = Image.open(file.file)
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img
    except:
        raise("Error loading image from client")
    finally:
        await file.close()

@router.post("/get_text", response_description="post images successfully")
async def text_detecting(
    front_image_file: UploadFile=File(...),
    inner_left_image_file: UploadFile=File(...), 
    inner_right_image_file: UploadFile=File(...), 
    back_image_file: UploadFile=File(...)
):
    pipeline = FullPipeline()
    try:
        front_image = await read_image(front_image_file)
        inner_left_image = await read_image(inner_left_image_file)
        inner_right_image = await read_image(inner_right_image_file)
        back_image = await read_image(back_image_file)

        data = pipeline(front_image, inner_left_image, inner_right_image, back_image)
        return data

    except:
        raise HTTPException(status_code=404, detail="Cannot get text from images")



