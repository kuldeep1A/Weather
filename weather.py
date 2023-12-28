import os

import dotenv
import requests

dotenv.load_dotenv()


def get_weather(city="Delhi"):
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    weather = requests.get(requests_url).json()
    return weather
