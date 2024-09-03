# Segmentation using YOLO
The code written for the segmentaion using YOLOv8m-seg. After segmentation of the receipts the segmented receipt will be passed to the OCR such that GPT4o. 


## Setup 
- Install Python 3.10.0
- Create the data folder and place the train, test and valid data (Each folder have images and labels folder)
- Create the virtual environment 

```shell
python -m venv app
```
- Install the requirements.txt 

```bash
pip install -r requirements.txt
```

- Run train_yolov8_seg file 

```shell
python src/train_yolov8_seg.py
``` 

- Test the segmentaion 

```shell
python src/test_model.py
```


### Dataset Directory Structure 
```bash
dataset/
│
├── train/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── labels/
│       ├── image1.txt
│       ├── image2.txt
│       └── ...
│
├── val/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── labels/
│       ├── image1.txt
│       ├── image2.txt
│       └── ...
│
└── test/
    ├── images/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── labels/
        ├── image1.txt
        ├── image2.txt
        └── ...

```
