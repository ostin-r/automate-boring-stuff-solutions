'''
getOpenWeather.py is a follow along project from Ch. 16
which downloads json weather data from OpenWeatherMap.org
and prints it to a text file
'''
import json, requests, sys, os
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')

if len(sys.argv) < 2:
    print('Usage: python getOpenWeather.py city_name')
    sys.exit()

with open('openWeather_APIKey.txt') as file:
    api_key = file.readline()

location = ' '.join(sys.argv[1:])
log.debug(location)

# Download json data from api
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
response = requests.get(url)
response.raise_for_status()