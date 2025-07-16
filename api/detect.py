from ultralytics import YOLO
import os

# Load model once
model = YOLO("yolov8n.pt")

def run_detection(video_path=None):
    if video_path is None:
        base_dir = os.path.dirname(__file__)
        video_path = os.path.join(base_dir, "videos", "sample.mp4")
    else:
        # convert to absolute if given as relative
        base_dir = os.path.dirname(__file__)
        video_path = os.path.join(base_dir, video_path)

    print("Final video path being used:", video_path)

    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"{video_path} does not exist")

    results = model.predict(source=video_path, save=True)

    return {
        "status": "success",
        "message": f"Detection completed on {video_path}"
    }
