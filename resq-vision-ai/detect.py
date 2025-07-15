from ultralytics import YOLO

# Load trained model (later you'll change to best.pt)
model = YOLO("yolov8n.pt")

# Run detection on a sample image
results = model.predict("data/sample.jpg", save=True)

print("✅ Detection complete! Results saved to 'runs/predict'")
