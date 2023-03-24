import os
from westeros_locations import get_westeros_location, format_descriptions, format_images
import requests
from flask import Flask, render_template, request
from ip2geotools.databases.noncommercial import DbIpCity

app = Flask(__name__,
            static_url_path='',
            template_folder='templates')

OPENWEATHER_API_KEY = 'af5530d3a91fc00839e65ec259c08e8d'
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

IMAGE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "static/images")

def get_weather_data(location):
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_WEATHER_URL, params=params)
    return response.json()


@app.route('/')
def index():
    ip_address = request.remote_addr
    location = DbIpCity.get(ip_address, api_key='free')
    weather_data = get_weather_data(location)

    descriptions = format_descriptions({}, "westeros_weather_descriptions.txt")
    images = format_images({}, IMAGE_FOLDER_PATH)
    westeros_location = get_westeros_location(weather_data, descriptions, images)

    return render_template('index.html', westeros_location=westeros_location['name'],
                           image_filename=westeros_location['image'],
                           description=westeros_location['description'],
                           temp_c=int(weather_data['main']['temp']),
                           temp_f=int(weather_data['main']['temp'] * 9 / 5 + 32),
                           weather_conditions=weather_data['weather'][0]['main'])



if __name__ == '__main__':
    app.run()
