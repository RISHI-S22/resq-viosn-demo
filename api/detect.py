import os
from ultralytics import YOLO
import requests

# Load model (you can change this to your actual model path)
model = YOLO("yolov8n.pt")

def run_detection(video_path=None):
    # If video_path not provided, use default sample.mp4 in videos folder
    if video_path is None:
        base_dir = os.path.dirname(__file__)
        video_path = os.path.join(base_dir, "videos", "sample.mp4")

    print("Final video path being used:", video_path)

    # Run detection and save results
    results = model.predict(source=video_path, save=True)

    # ✅ Send alert after detection (dummy alert to httpbin.org)
    alert_data = {
        "message": f"Detection completed on {video_path}",
        "status": "detected"
    }
    try:
        response = requests.post("https://httpbin.org/post", json=alert_data)
        print("Alert sent! Response status:", response.status_code)
    except Exception as e:
        print("Failed to send alert:", e)

    # Return result summary
    return {
        "status": "success",
        "message": f"Detection completed on {video_path}"
    }
