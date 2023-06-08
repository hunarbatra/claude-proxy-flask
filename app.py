from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/proxy": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/proxy', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
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
