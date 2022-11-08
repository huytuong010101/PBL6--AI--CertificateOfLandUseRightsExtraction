from modules.text_detection import TextDetection    
from modules.text_recognition import TextRecognition
from modules.information_extraction import InformationExtraction
from PIL import Image 
import cv2
import json

if __name__ == "__main__":
    detector = TextDetection(device="cpu")
    recognizer = TextRecognition(device="cpu")
    extractor = InformationExtraction()
    
    front_image = cv2.imread(r"samples/front.png")
    inner_left_image = cv2.imread(r"samples/inner_left.jpg")
    inner_right_image = cv2.imread(r"")
    back_image = cv2.imread(r"")
    
    front_text, inner_left_text, inner_right_text, back_text = "", "", "", ""
        
    if front_image is not None:
        print(">> Process on front")
        for i, line in enumerate(detector(front_image)):
            line_text = ""
            for bbox, image in line:
                text, confidence = recognizer(Image.fromarray(image))
                line_text = line_text + text
            print(">>", line_text)
            front_text = front_text + line_text + "\n"
            
    if inner_left_image is not None:
        print(">> Process on inner left")
        for i, line in enumerate(detector(inner_left_image)):
            line_text = ""
            for bbox, image in line:
                text, confidence = recognizer(Image.fromarray(image))
                line_text = line_text + text
            print(">>", line_text)
            inner_left_text = inner_left_text + line_text + "\n"   
            
    data = extractor(front=front_text, inner_left=inner_left_text, is_debug=False)
    print(json.dumps(data, indent=4, ensure_ascii=False))