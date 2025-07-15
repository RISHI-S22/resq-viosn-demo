from ultralytics import YOLO

# Load a pretrained YOLOv8 model (nano version)
model = YOLO('yolov8n.pt')

# Train

results = model.train(
    data='data.yaml',
    epochs=10,
    imgsz=640
)
