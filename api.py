from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) 

# Your WeatherAPI key
api_key = '35ddcd48136b4335ae832158240710'

# Define a route to fetch Hyderabad weather
@app.route('/')
def get_weather():
    try:
        # API URL for current weather data in Hyderabad
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Hyderabad"
        
        # Making the API request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return jsonify(data), 200
        else:
            return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app on Render's specified port (Render will set PORT environment variable)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

