from flask import Flask, request, jsonify
from detect import run_detection
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'videos')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def home():
    return "ResQ Vision API is running!"

@app.route('/detect', methods=['POST'])
def detect_accident():
    data = request.get_json()
    video_path = None
    if data:
        video_path = data.get('video_path')
    result = run_detection(video_path)
    return jsonify(result)

# 🌟 New: upload endpoint
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part in request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400
    
    # Save file
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)
    
    return jsonify({'status': 'success', 'message': f'File uploaded as {file.filename}'})
if __name__ == "__main__":
    app.run(debug=False)

