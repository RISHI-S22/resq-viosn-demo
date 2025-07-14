```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ResQ Vision backend running"}

@app.get("/detect")
def detect_accident():
    # TODO: integrate AI model here
    return {"detected": False, "confidence": 0.0}

@app.post("/alert")
def send_alert(location: str):
    # TODO: send alert to police/hospital
    return {"status": "Alert sent", "location": location}

@app.get("/status")
def status():
    return {"service": "online"}