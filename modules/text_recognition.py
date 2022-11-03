import sys
if "../" not in sys.path:
    sys.path.append("../")
from modules.Base import Base
from config import text_recognition_config_yml_path, text_recognition_weights_path
from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor
import gdown
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"


class TextRecognition(Base):
    def __init__(self, model_name='vgg_transformer', device="cpu", get_config_yml=False):
        if not os.path.exists(text_recognition_weights_path):
            self.get_weights_from_gdrive()
        if not os.path.exists(text_recognition_config_yml_path) and get_config_yml == True:
            self.get_config_yml_from_gdrive()
            config = Cfg.load_config_from_file(text_recognition_config_yml_path)
        else:
            config = Cfg.load_config_from_name(model_name)
        config['device'] = device
        config['weights'] = text_recognition_weights_path
        self.recognizer = Predictor(config)

    def get_config_yml_from_gdrive(self, url='https://drive.google.com/uc?id=156WvR35nXeAIzYWLi1Rw1xQWu0uSMKXp'):
        output = text_recognition_config_yml_path
        gdown.download(url, output, quiet=False)

    def get_weights_from_gdrive(self, url='https://drive.google.com/uc?id=15NTDP5PY1SZY0jz_o2Vc0TXq0S8-YYZC'):
        output = text_recognition_weights_path
        gdown.download(url, output, quiet=False)

    def __call__(self, img):
        text, confidence = self.recognizer.predict(img, return_prob=True)
        return text, confidence
        

    