from ultralytics import YOLO


# Load the YOLOv8m model pre-trained on the COCO dataset
model = YOLO('yolov8m-seg.pt')  # Using YOLOv8 medium model for segmentation

# Train the model
model.train(
    data='dataset.yaml',  # Path to your dataset YAML file
    epochs=100,            # Number of epochs
    imgsz=1024,             # Image size
    batch=8,              # Batch size
    name='yolov8m-seg-receipts',  # Experiment name
    project='runs/train',  # Save results in the 'runs/train' directory
    task='segment',        # Task type: 'segment' for segmentation
    workers=4              # Number of worker threads for data loading
)
