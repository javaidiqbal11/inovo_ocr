from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load the trained YOLOv8m segmentation model
model = YOLO('runs/train/yolov8m-seg-receipts/weights/best.pt')  # Path to the best model weights

# Load the image for testing
image_path = 'data/test/images/image1.jpg'
image = cv2.imread(image_path)

# Perform segmentation
results = model.predict(source=image_path, save=True, task='segment')

# Visualize the results
annotated_image = results[0].plot()  # Get the annotated image

# Display the annotated image
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
