import dotenv
import requests
import os
from pprint import pprint
dotenv.load_dotenv()

def get_weather(city="Delhi"):
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}"
    weather = requests.get(requests_url).json()
    return weather

if __name__ == "__main__":
    print('\n*** Get Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")


    weather_data = get_weather(city)

    print("\n")
    pprint(weather_data)