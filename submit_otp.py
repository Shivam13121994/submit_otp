from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to submit OTP
@app.route('/submit-otp', methods=['POST'])
def submit_otp():
    # Replace with your actual server URL if different
    url = 'https://sandbox.surepass.io/api/v1/aadhaar-v2/submit-otp'
    
    # Replace with your actual Bearer token
    TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTI5NjczNCwianRpIjoiNWE4NTNiOGQtNjkwZC00ZjQwLWI1ODktNmVlMTAzMzdkZWViIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LmNvbnNvbGVfMnVsOWRtbnFmMnhmOWFqaGFlY2R0Y3UzcGM5QHN1cmVwYXNzLmlvIiwibmJmIjoxNzE5Mjk2NzM0LCJleHAiOjE3MTk3Mjg3MzQsImVtYWlsIjoiY29uc29sZV8ydWw5ZG1ucWYyeGY5YWpoYWVjZHRjdTNwYzlAc3VyZXBhc3MuaW8iLCJ0ZW5hbnRfaWQiOiJtYWluIiwidXNlcl9jbGFpbXMiOnsic2NvcGVzIjpbInVzZXIiXX19.4VqaSsM3G_xKtBCWnz6ux8X41A-vyI9bNg84XpYBGSM'
    
    # Parse JSON data from request
    request_data = request.get_json()
    
    # Extract client_id and otp from JSON payload
    client_id = request_data.get('client_id', '')
    otp = request_data.get('otp', '')
    
    # Prepare payload and headers
    payload = {
       "client_id": client_id,
       "otp": otp
    }
    
    headers = {
       'Content-Type': 'application/json',
       'Authorization': f'Bearer {TOKEN}'
    }
    
    # Make POST request to external API
    response = requests.post(url, json=payload, headers=headers)
    
    # Process response from external API
    if response.status_code == 200:
       return jsonify({
           'status': 'success',
           'message': 'OTP submission successful!',
           'response': response.json()
       }), 200
    else:
       return jsonify({
           'status': 'error',
           'message': 'Failed to submit OTP',
           'response_code': response.status_code,
           'response_message': response.text
       }), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0")
