# Building module to extract information from Land Registration
## Project tree
```
.
├── config                  # Contain all configuration for training or testing
├── core                    # 
│   ├── model               # Define model construction here
│   └── loss                # Define loss function here
├── data_processing         # Function to process data (Download, preprocess, create anotation,...) 
├── modules                 # The Class which use to inference, must extend from Base.py
├── samples                 # Just some samples data
└── tools                   # All script can running are here (train, test, inferrence, evaluate, process data,...)
```
## Training
### OCR
- Config
 + Config the path where downloaded files are located in config/production_config.py
 + Example:
 ```
    # Path to config.yml file 
    text_recognition_config_yml_path = '/home/hanlhn/Downloads/config.yml'
    # Path to weights file
    text_recognition_weights_path = '/home/hanlhn/Downloads/transformerocr.pth'
 ```
- Create annotation: ...
- Training: `python3 ...`
## Evaluate
### OCR
## Start training VietOCR
```python3 tools/train_ocr.py <your_dataset_path>
   # Example: python3 tools/train_ocr.py "/home/hanlhn/Downloads/dataset-20221118T073324Z-001/dataset/"
```
## Start evaluating VietOCR
```python3 tools/eval_ocr.py <your_dataset_path>
   # Example: python3 tools/train_ocr.py "/home/hanlhn/Downloads/dataset-20221118T073324Z-001/dataset/"
```
## Inference
### Text detection
- `python3 tools/infer_text_detection.py`
### OCR
- `python3 tools/infer_text_recoginition.py`
### Information extraction
- `python3 tools/infer_information_extraction.py`

## Start serving API
- `python3 tools/serving.py`

