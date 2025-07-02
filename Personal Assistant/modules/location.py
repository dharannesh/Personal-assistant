import requests

def get_current_city():
    try:
        response = requests.get("https://ipapi.co/json/")
        data = response.json()
        return data.get("city", "Chennai")  
    except:
        return "Chennai"  
