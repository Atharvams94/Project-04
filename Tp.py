import numpy as np

def fft(data):
if analysis_results:
  print("Analysis Results:")
  
  import aiohttp
import aiofiles
import asyncio
import json
from datetime import datetime


    async def fetch_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    response.raise_for_status()

    async def save_weather_data(self, city, data):
        filename = f"{city}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        async with aiofiles.open(filename, 'w') as file:
            await file.write(json.dumps(data, indent=4))
        print(f"Weather data saved to {filename}")


    
            print(f"Error fetching weather data for {city}: {e}")

async def main():
    api_key = 'your_openweathermap_api_key'  # Replace with your actual API key
    cities = ['London', 'New York', 'Tokyo', 'Sydney']

    weather_fetcher = WeatherFetcher(api_key)
    tasks = [weather_fetcher.get_and_save_weather(city) for city in cities]
    await asyncio.gather(*tasks)



