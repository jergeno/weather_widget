#!/usr/bin/python3


# A tool to poll Open Weather Map and display the results
# Author: Jeremy Genovese
# Date Created: 3-4-2021
# Version: 0.1
#TODO: refactor the code into functional blocks. IN PROGRESS

import json
import requests
import yaml

cities=[]
CITY_ID = {'Ypsilanti' : '5015688', 'Ann Arbor' : '4984247', 'Whitmore Lake' : '5014946', 'Midland' : '5001929'}

# load the configuration
with open("config.yaml") as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)
    
# get the city id
with open("city.list.json") as city_list_file:
    cities=json.load(city_list_file)
print(type(cities))
citySubList = []
for item in cities:
    if item["name"] == "Midland":
        citySubList.append(item)
print("Did you mean: ")
for item in citySubList:
     print("{}. {}, {}, {}".format(citySubList.index(item), item["name"], item["state"], item["country"]))
city = citySubList[int(input("Enter your choice: "))]
print(city["id"])

        
# TODO: next steps are to ship printing state if it is empty, and then move on to actually accepting user input ans returning the city id

    
# get the city from the user
def get_city_from_user():
    print('Select a city from the following options: ')
    for city in CITY_ID:
        print(city)
    selected_city = input()
    city_num = CITY_ID[selected_city]
    return city_num
    
# download the json object and return its text as a dictionary object
def get_API_data(key, city_id):
    response = requests.get(config["api_url"].format(city_id, key, config["units"]))  # get the data and begin processing
    weather_text = json.loads(response.text)
    return weather_text


# break out the data into discrete variables WIP
def parse_and_print_data(weather_dict_object):
    current_city = weather_dict_object['name']
    current_temp = weather_dict_object['main']['temp']
    current_humidity = weather_dict_object['main']['humidity']
    current_feel = weather_dict_object['main']['feels_like']
    current_wind_speed = weather_dict_object['wind']['speed']
    # if gust in weather: #TODO: Figure out an elegant way to check for the existence of a key. 'gust' is not always present
    #     current_wind_gust = weather['wind']['gust']
    # else:
    #     pass
    # display the output to the user
    print()
    print("Currently in {}:\nTemperatrure: {} F\nHumidity: {}%\nFeels Like: {} F".format(current_city, current_temp, current_humidity, current_feel))
    print("The wind speed is: {} mph".format(current_wind_speed))

# main method
def main():
    city_id_num = get_city_from_user()
    weather = get_API_data(config["api_key"], city_id_num)
    parse_and_print_data(weather)

# fire missiles!
#main()

