# modules/weather.py
import requests

def get_weather(city="Chennai"):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text

def get_weather_in_current_location():
    from modules.location import get_current_city
    city = get_current_city()
    return get_weather(city)
