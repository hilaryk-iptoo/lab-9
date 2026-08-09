import httpx
import os


WEATHER_API_URL = os.getenv(
    "WEATHER_API_URL",
    "https://api.open-meteo.com/v1/forecast"
)


async def get_weather(
    latitude: float,
    longitude: float
):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            WEATHER_API_URL,
            params=params,
            timeout=10.0
        )

        response.raise_for_status()

        return response.json()