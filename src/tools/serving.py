from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
import uvicorn
import numpy as np
import cv2
from modules.full_pipeline import FullPipeline

async def file2opencv(file):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

app = FastAPI()
pipeline = FullPipeline()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def extract_info(
    img_front: UploadFile=File(),
    img_back: UploadFile=File(),
    img_inner_left: UploadFile=File(),
    img_inner_right: UploadFile=File(),
    ):
    front_image = await file2opencv(img_front)
    back_image = await file2opencv(img_back)
    inner_left_image = await file2opencv(img_inner_left)
    inner_right_image = await file2opencv(img_inner_right)
    data = pipeline(front_image, inner_left_image, inner_right_image, back_image)
    return data
    
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")