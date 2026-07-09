import requests
from .weather_codes import WEATHERCODE

class WeatherAgent:
    def __init__(self, ):
        pass
        
    def search(self,latitude,longitude):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max"
            "&forecast_days=10"
            "&timezone=auto"
        )
        response = requests.get(url).json()
        return response
    
    
    def extract_data(self, data, date):
        times = data["daily"]["time"]

        if date not in times:
            return None

        index = times.index(date)
        weather_code = data['daily']['weathercode'][index]
        max_temp = data['daily']['temperature_2m_max'][index]
        min_temp = data['daily']['temperature_2m_min'][index]
        precipitation_probability = data['daily']['precipitation_probability_max'][index]
        weather = WEATHERCODE.get(weather_code)
        return {
            "weather_code": weather_code,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "precipitation_probability": precipitation_probability,
            "weather": weather
        }
        
        
        
# weather = WeatherAgent()
# data = weather.search(11.42355, 76.684494)
# ans = weather.extract_data(data, '2026-07-10')
# print(ans)