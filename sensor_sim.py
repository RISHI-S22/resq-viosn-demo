import time
import random
import requests

BACKEND_URL = "https://resvi.onrender.com"
SENSOR_ID = "LP-12"  # Light pole sensor id

while True:
    data_value = round(random.uniform(0.0, 10.0), 2)  # Fake vibration or impact
    try:
        r = requests.post(f"{BACKEND_URL}/report?sensor_id={SENSOR_ID}&data={data_value}")
        print(f"Sent: {data_value} → Response: {r.json()}")
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # Wait 5 seconds before next reading
