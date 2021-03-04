# A tool to poll Open Weather Map and display the results
# Author: Jeremy Genovese
# Date Created: 3-4-2021
# Version: 0.1
#TODO: refactor the code into functional blocks

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

# store the desired parameters into their own variables

current_city = weather['name']
current_temp = weather['main']['temp']
current_humidity = weather['main']['humidity']
current_feel = weather['main']['feels_like']
current_wind_speed = weather['wind']['speed']
current_wind_gust = weather['wind']['gust']
# display the output to the user
print("Currently in {}:\nTemperatrure: {} F\nHumidity: {}%\nFeels Like: {} F".format(current_city, current_temp, current_humidity, current_feel))
print("The wind speed is: {} mph, with gusts to {} mph".format(current_wind_speed, current_wind_gust))