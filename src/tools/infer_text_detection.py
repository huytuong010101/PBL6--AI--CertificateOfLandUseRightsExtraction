from modules.text_detection import TextDetection    
import cv2

IMG_PATH = r"samples/inner_left.jpg"

if __name__ == "__main__":
    detector = TextDetection(device="cpu")
    
    image = cv2.imread(IMG_PATH)
    clone_image = image.copy()
    image = image[:, :, ::-1]
    clone_image = image.copy()

    for i, line in enumerate(detector(image)):
        line_text = ""
        for bbox, image in line:
            clone_image = cv2.polylines(clone_image, [bbox], isClosed=True, color=(255, 0, 0), thickness=1)
            
    cv2.imshow("result", clone_image)
    cv2.waitKey(0)