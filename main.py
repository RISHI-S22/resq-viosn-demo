from fastapi import FastAPI
from datetime import datetime
import os
import json
import random

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "running"}

@app.get("/detect")
def detect():
    return {"detected": random.choice([True, False]), "confidence": random.uniform(0.5, 1.0)}

@app.post("/report")
def report(sensor_id: str, data: float):
    report = {"sensor_id": sensor_id, "data": data, "timestamp": datetime.now().isoformat()}

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
        print("Error saving report:", e)

    return {"message": "Data received", "report": report}

@app.post("/alert")
def alert(location: str):
    # Fake alert logic
    return {"message": f"Alert sent to nearby responders for location: {location}"}

@app.get("/get-reports")
def get_reports():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            data = json.load(f)
        return {"reports": data}
    else:
        return {"reports": []}
