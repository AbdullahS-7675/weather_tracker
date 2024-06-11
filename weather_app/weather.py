import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:float

def get_lan_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    if resp:
        data = resp[0]
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    else:
        return None, None #always return a tuple, even when no data found

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperature = resp.get('main').get('temp')
    )
    return data

def get_weather(city_name, state_name, country_name):
    lat, lon = get_lan_lon(city_name, state_name, country_name, api_key)
    if lat == None: #only need to check lat or lon
        return None
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

#for testing purposes
if __name__ == "__main__":
    print(get_weather('freferf', 'frfioe', 'frfir'))