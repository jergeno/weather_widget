# A tool to poll Open Weather Map and display the results
# Author: Jeremy Genovese
# Date Created: 3-4-2021
# Version: 0.1
#TODO: refactor the code into functional blocks. IN PROGRESS

import json
import requests

API_KEY_FILE = "/home/hiro/bin/weather_widget/openWeatherMap_API_key"
API_URL = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}"
CITY_ID = {'Ypsilanti' : '5015688', 'Ann Arbor' : '4984247', 'Whitmore Lake' : '5014946', 'Midland' : '5001929'}
DEFAULT_UNITS = "imperial"

# get the API key
def Get_API_key(keyfile):
    with open(keyfile, "r") as API_file:
        key = API_file.readline()
        API_file.close()
    return key

def Get_city_from_user():
    print('Select a city from the following options: ')
    for city in CITY_ID:
        print(city)
    selected_city = input()
    city_num = CITY_ID[selected_city]
    return city_num
    

def Get_API_data(key, city_id):
    response = requests.get(API_URL.format(city_id, key, DEFAULT_UNITS))  # get the data and begin processing
    weather_text = json.loads(response.text)
    return weather_text


def main():
    api_key = Get_API_key(API_KEY_FILE)
    city_id_num = Get_city_from_user()
    weather = Get_API_data(api_key, city_id_num)
    return weather
weather = main()


# debugging
# print(weather)

# store the desired parameters into their own variables

current_city = weather['name']
current_temp = weather['main']['temp']
current_humidity = weather['main']['humidity']
current_feel = weather['main']['feels_like']
current_wind_speed = weather['wind']['speed']
# if gust in weather: #TODO: Figure out an elegant way to check for the existence of a key. 'gust' is not always present
#     current_wind_gust = weather['wind']['gust']
# else:
#     pass
# display the output to the user
print()
print("Currently in {}:\nTemperatrure: {} F\nHumidity: {}%\nFeels Like: {} F".format(current_city, current_temp, current_humidity, current_feel))
print("The wind speed is: {} mph".format(current_wind_speed))
