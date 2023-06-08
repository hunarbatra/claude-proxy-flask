from flask import Flask, request
from flask_cors import CORS
import requests

# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)

# run_with_ngrok(app)

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'POST':
        req_data = request.get_json()
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': request.headers.get('x-api-key')
        }
        response = requests.post('https://api.anthropic.com/v1/complete', json=req_data, headers=headers)
        return response.json()
    else:
        return {'error': 'This endpoint supports only POST requests'}

if __name__ == '__main__':
    app.run(port=5000)