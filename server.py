from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes so your frontend can talk to it!

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Calculator backend is online!"}), 200

@app.route('/solve', methods=['POST'])
def solve_equation():
    data = request.json
    equation = data.get('equation', '')
    
    if not equation:
        return jsonify({'error': 'No equation provided'})

    try:
        process = subprocess.Popen(
            ['./calculator'], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        stdout, stderr = process.communicate(input=equation + '\n')
        
        return jsonify({'response': stdout.strip()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
