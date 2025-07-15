from ultralytics import YOLO

# Load the trained model
model = YOLO('runs/detect/train10/weights/best.pt')

# Run detection on images in folder
results = model.predict(source='images/train', show=True, save=True)


print("Detection complete! Check the 'runs/detect/predict' folder for results.")
