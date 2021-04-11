'''
getOpenWeather.py is a follow along project from Ch. 16
which downloads json weather data from OpenWeatherMap.org
and prints it to a text file
'''
import json, requests, sys, os

if len(sys.argv) < 2:
    print('Usage: python getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

api_key = open('openWeather_APIKey.txt').readline()
location = ' '.join(sys.argv[1:])

# Download json data from api
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={api_key}'
response = requests.get(url)
response.raise_for_status()