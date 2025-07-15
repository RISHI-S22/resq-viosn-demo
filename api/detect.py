# api/detect.py

def run_detection(video_path):
    """
    Dummy detection function. Later this will load a trained AI model 
    and run inference on the video.
    """
    print(f"Running detection on: {video_path}")
    # Simulate result
    return {"status": "success", "message": f"Detected accident in {video_path}"}
