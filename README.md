# Segmentation using YOLO

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
