from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ResQ Vision backend running"}

@app.get("/detect")
def detect_accident():
    # TODO: integrate AI model here
    # For now, return mock detection
    return {"detected": True, "confidence": 0.82}

@app.post("/alert")
def send_alert(location: str):
    # TODO: actually send alert
    return {"status": "Alert sent successfully", "location": location}

@app.get("/status")
def status():
    return {"service": "online"}
