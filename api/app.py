from flask import Flask, request, jsonify
from detect import run_detection  # import our function

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_accident():
    """
    Call detect.py with the provided video path.
    """
    data = request.json
    video_path = data.get('video_path')
    
    if not video_path:
        return jsonify({"status": "error", "message": "Missing video_path"}), 400

    result = run_detection(video_path)
    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return "ResQ Vision API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
