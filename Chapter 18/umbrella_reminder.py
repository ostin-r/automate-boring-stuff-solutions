'''
Austin Richards 5/3/21

umbrella_reminder.py checks weather.gov if it is going to rain today.
If it is going to rain today, it will send a text reminder to my 
cell phone to remind me to bring an umbrella.

This program will be set up to run every day using microsoft's built-
in Task Scheduler program.
'''
import requests, json, pprint
from twilio_test import send_text

# get credentials, location
api_key, location = open('weather_creds.txt').read().splitlines()

# get local weather
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
res = requests.get(url)
res.raise_for_status()

weather_data = json.loads(res.text)
#weather = weather_data['weather'][0]['description']
weather = 'light rain' # for testing...

# send a text if it will rain today
if 'rain' in weather: send_text("Don't forget an umbrella today! Rain is in the forecast.")