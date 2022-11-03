# Xây dụng module trích xuất thông tin từ sổ đỏ
## Cấu trúc thư mục
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
- Config ...
- Create anotation: ...
- Training: `python3 ...`
## Evaluate
### OCR
## Inference
### Text detection
- `python3 tools/infer_text_detection.py`
### OCR
### Information extraction
- `python3 tools/infer_information_extraction.py`
