from modules.text_recognition import TextRecognition
import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import cv2

IMG_PATH = r"samples/ocr.jpg"

if __name__ == "__main__":
    recognizer = TextRecognition(device="cpu")
    image = cv2.imread(IMG_PATH)
    image = image[:, :, ::-1]
    text, confidence = recognizer(Image.fromarray(image))
    title = "Text: " + str(text) + " - Confidence: " + str(confidence)
    print(title)
    cv2.imshow("image", image)
    cv2.waitKey(0)