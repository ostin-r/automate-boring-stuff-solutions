'''
getOpenWeather.py is a follow along project from Ch. 16
which downloads json weather data from OpenWeatherMap.org
and prints it to a text file
'''
import json, requests, sys, os, pprint
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')
log.disable(log.CRITICAL)


def convertKF(temp_K):
    temp_F = (temp_K - 273.15) * (9/5) + 32
    return round(temp_F, 2)


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

# change the weather data from json to python dict
weather_data = json.loads(response.text)
pprint.pprint(weather_data)

description = weather_data['weather'][0]['description']
temp = convertKF(weather_data['main']['temp'])
feels_like = convertKF(weather_data['main']['feels_like'])
humidity = weather_data['main']['humidity']
country = weather_data['sys']['country'] 

print(f'\nCurrent weather for {location}, {country}:')
print(f'Description: {description}')
print(f'Temperature: {temp} F')
print(f'Feels Like: {feels_like} F')