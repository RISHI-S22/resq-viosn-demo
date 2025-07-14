from ultralytics import YOLO

# 🚀 Load a pretrained YOLOv8 model (e.g., yolov8n - nano version, fastest)
model = YOLO("yolov8n.pt")

# ✅ Train on your dataset
# data.yaml should describe your dataset (we'll create it)
results = model.train(
    data="data/data.yaml",   # path to dataset config
    epochs=20,               # number of epochs
    imgsz=640                # image size
)

print("✅ Training complete!")
