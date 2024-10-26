# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/vrchat-info', methods=['GET'])
def get_vrchat_info():
    user_id = request.args.get('usr_bd93e462-442f-4977-bc30-2b513997b9d9')
    headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfYmQ5M2U0NjItNDQyZi00OTc3LWJjMzAtMmI1MTM5OTdiOWQ5IiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTcyNjQ3NTQwNzI1MiwidmVyc2lvbiI6MSwiaWF0IjoxNzI5ODkyOTIxLCJleHAiOjE3MzI0ODQ5MjEsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.xWf7xnRrllclandGAXbuLuWMZ4vNNstqx4ohWEfz8H8'}  # Remplace par ton token VRChat
    response = requests.get(f'https://api.vrchat.cloud/api/1/users/{user_id}', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "status": data.get("status"),
            "location": data.get("location")
        })
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
