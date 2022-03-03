#!/usr/bin/python3


# A tool to poll Open Weather Map and display the results
# Author: Jeremy Genovese
# Date Created: 3-4-2021
# Version: 0.2
#TODO: refactor the code into functional blocks. IN PROGRESS

import json
import re
import requests
import yaml

# load the configuration
with open("config.yaml") as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)

# load the city list
with open("city.list.json") as city_list_file:
    cities=json.load(city_list_file)

# TODO: change to return the lat and long from the city
# get the city id
def get_city():
    userCity = input("Please enter a city name: ")
    citySubList = []
    for item in cities:
        if item["name"].casefold() == userCity.casefold():
            citySubList.append(item)
    if len(citySubList) == 0:
        print("City not found!")
        exit(0)
    elif len(citySubList) > 1:
        print("Did you mean: ")
        for item in citySubList:
            print("{}. {}, {}, {}".format(citySubList.index(item), item["name"], item["state"], item["country"]))
        city = citySubList[int(input("Enter your choice: "))]
    else:
        city = citySubList[0]
    return city

        
# TODO: next steps are to skip printing state if it is empty

# download the json object and return its text as a dictionary object
# see OpenWeatherMap API docs at https://openweathermap.org/api/one-call-api for information
def get_API_data(key, city_object, exclude):
    response = requests.get(config["api_url"].format(city_object["coord"]["lat"], city_object["coord"]["lon"], exclude, key, config["units"]))  # get the data and begin processing
    weather_text = json.loads(response.text)
    return weather_text


# break out the data into discrete variables WIP
def parse_and_print_data(weather_object, city_object):
    current_city = city_object["name"] 
    current_temp = weather_object["current"]["temp"]
    current_humidity = weather_object["current"]["humidity"]
    current_feel = weather_object["current"]["feels_like"]
    current_wind_speed = weather_object["current"]["wind_speed"]
    daily_high = weather_object["daily"][0]["temp"]["max"]
    daily_low = weather_object["daily"][0]["temp"]["min"]
    tomorrow_high = weather_object["daily"][1]["temp"]["max"]
    tomorrow_low = weather_object["daily"][1]["temp"]["min"]
    # if gust in weather: #TODO: Figure out an elegant way to check for the existence of a key. 'gust' is not always present
    #     current_wind_gust = weather['wind']['gust']
    # else:
    #     pass
    # display the output to the user
    print()
    print("Currently in {}:\nTemperatrure: {} F\nHumidity: {}%\nFeels Like: {} F".format(current_city, current_temp, current_humidity, current_feel))
    print("Wind Speed: {} mph".format(current_wind_speed))
    print("High: {} F\nLow: {} F".format(daily_high, daily_low))
    print("\nTomorrow's Forecast")
    print("High: {} F\nLow: {} F".format(tomorrow_high, tomorrow_low))

# main method
def main():
    city = get_city()
    weather = get_API_data(config["api_key"], city, "minutely") 
    parse_and_print_data(weather, city)

# fire missiles!
main()

