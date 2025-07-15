from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_accident():
    """
    Placeholder detection endpoint.
    Later, this will call detect.py and return the detection result.
    """
    # data = request.json
    # result = run_detection(data)
    # return jsonify(result)
    return jsonify({"status": "success", "message": "Accident detection simulated."})

@app.route('/', methods=['GET'])
def home():
    return "ResQ Vision API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
