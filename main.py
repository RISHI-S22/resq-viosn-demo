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
def report(sensor_id: str, data: float):
    report = {"sensor_id": sensor_id, "data": data, "timestamp": datetime.now().isoformat()}
    
    # Save to file
    try:
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                all_reports = json.load(f)
        else:
            all_reports = []

        all_reports.append(report)
        with open("data.json", "w") as f:
            json.dump(all_reports, f, indent=2)
    except Exception as e:
        print("Failed to save:", e)

    return {"message": "Data received", "report": report}
