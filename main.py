# A tool to poll Open Weather Map and display the results
# Author: Jeremy Genovese
# Date Created: 3-4-2021
# Version: 0.1

import json
import requests

API_KEY_FILE = "/home/hiro/bin/weather_widget/openWeatherMap_API_key"
API_URL = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}"
CITY_ID = "5014946" # Whitmore Lake
DEFAULT_UNITS = "imperial"

# get the API key
with open(API_KEY_FILE, "r") as API_file:
    api_key = API_file.readline()
    API_file.close()


response = requests.get(API_URL.format(CITY_ID, api_key, DEFAULT_UNITS))  # get the data and begin processing

weather = json.loads(response.text)
# debugging
print(weather)

print(weather['main']['temp'])