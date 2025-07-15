
# ResQ Vision AI

An AI-powered system to detect vehicle and pedestrian accidents from CCTV footage and instantly alert nearby police stations and hospitals.  
Built with deep learning and real-time dashboards for emergency response automation.

## 🌟 Features

- Accident detection using YOLOv8 object detection.
- Real-time video feed and alerts.
- Dashboard showing:
  - Accident status
  - Nearby police stations & hospitals
  - Latest alerts & saved video clips
- Automatic data push to backend API.
- Scalable architecture suitable for cloud deployment.

---

## 🛠️ Project Structure

```plaintext
resq-viosn-demo/
├── app.py                 # Main FastAPI / Flask application
├── dashboard.py           # Dashboard visualization
├── sensor_sim.py          # Simulated IoT sensor inputs
├── resq-vision-ai/        # AI model, dataset and training scripts
│   ├── train.py           # Model training script
│   ├── data.yaml          # Dataset config
│   └── ...
├── images/                # Collected and labeled images
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Files ignored by Git
└── LICENSE                # All rights reserved license
````

---

## ✅ How to set up & run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/RISHI-S22/resq-viosn-demo.git
cd resq-viosn-demo
```

### 2️⃣ Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/Scripts/activate    # Windows
# OR
source venv/bin/activate       # Linux/Mac

pip install -r requirements.txt
```

### 3️⃣ Train the AI model (if needed)

Make sure your dataset paths in `data.yaml` are correct.

```bash
cd resq-vision-ai
python train.py
```

### 4️⃣ Run the app

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:8000` (or your configured port).

---

## 🔄 Typical workflow to update & push

```bash
# Stage changes
git add .

# Commit changes
git commit -m "Describe your changes here"

# Push to GitHub
git push origin main
```

---

## ⚡ How to restart everything

If your PC restarts or you close terminal:

1. Open terminal in project folder
2. Activate virtual environment:

```bash
source venv/Scripts/activate    # Windows
# OR
source venv/bin/activate       # Linux/Mac
```

3. Run your app again:

```bash
python app.py
```

---

## 📜 License

All rights reserved © 2025 **Rishik Srivathsava**.
You may view the code, but copying, modifying, or distributing it is **not allowed** without permission.

---

## ✏️ Author

Built with ❤️ by **Rishik Srivathsava**.

````
> *Built with ❤️ for ResQ Vision*

 ## 📞 Contact
[LinkedIn]: www.linkedin.com/in/
rishik-srivathsava-059783310
 | Email: thalluririshi24@gmail.com
