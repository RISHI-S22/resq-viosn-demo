from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ResQ Vision backend running"}

@app.get("/detect")
def detect_accident():
    """
    Fake AI: randomly detect accident with some confidence
    """
    detected = random.choice([True, False])
    confidence = round(random.uniform(0.6, 0.99), 2) if detected else round(random.uniform(0.0, 0.4), 2)
    return {"detected": detected, "confidence": confidence}

@app.post("/alert")
def send_alert(location: str):
    """
    Pretend to send alert to police/hospital
    """
    return {"status": "Alert sent successfully", "location": location}

@app.get("/status")
def status():
    return {"service": "online"}

@app.post("/report")
def report_sensor_data(sensor_id: str, data: float):
    """
    Simulate sensor data report (e.g., impact force, vibration etc.)
    """
    # In future, process this data to help accident detection
    return {"status": "Data received", "sensor_id": sensor_id, "value": data}
