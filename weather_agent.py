import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_data(location):

    if not location or location == "Unknown":
        location = "Hyderabad"

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={location}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:

            return {

                "condition": "Unavailable",

                "temperature": "N/A",

                "alert": "Weather data unavailable"
            }

        weather_condition = data["weather"][0]["main"]

        temperature = data["main"]["temp"]

        alert = "Safe conditions"

        if weather_condition.lower() in [
            "storm",
            "thunderstorm",
            "rain"
        ]:

            alert = "Possible route disruptions"

        return {

            "condition": weather_condition,

            "temperature": temperature,

            "alert": alert
        }

    except Exception:

        return {

            "condition": "Unavailable",

            "temperature": "N/A",

            "alert": "Weather service error"
        }