import numpy as np
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import cv2
import face_recognition



# Draw a box around the face if a match is found
if results[0]:
    cv2.rectangle(image, (face_locations[0][0], face_locations[0][1]), (face_locations[0][2], face_locations[0][3]), (0, 0, 255), 2)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load image
image = cv2.imread("path/to/your/image.jpg")

# Detect faces in the image
face_locations = face_recognition.face_locations(image)

# Encode facial features
face_encodings = face_recognition.face_encodings(image, face_locations)

# Load a known image for comparison
known_image = cv2.imread("path/to/known_face.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Compare faces
results = face_recognition.compare_faces([known_face_encoding], face_encodings[0])

# Draw a box around the face if a match is found
if results[0]:
    cv2.rectangle(image, (face_locations[0][0], face_locations[0][1]), (face_locations[0][2], face_locations[0][3]), (0, 0, 255), 2)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



weather_data = analyze_weather_data(city, start_date, end_date)

# Data analysis and visualization
print(weather_data.describe())

plt.figure(figsize=(10, 6))
plt.plot(weather_data["Date"], weather_data["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature (K)")
plt.title(f"Temperature in {city}")
plt.show()

sns.pairplot(weather_data[["Temperature", "Humidity", "Pressure", "Wind Speed"]])
plt.show()

correlation_matrix = weather_data[["Temperature", "Humidity", "Pressure", "Wind Speed"]].corr()
print(correlation_matrix)
def fft(data):
  
  return np.fft.fft(data)


  try:
    with open(data_file, 'r') as f:
      data = f.readlines()
  except FileNotFoundError:
    print(f"Error: File {data_file} not found.")
    return None

  # Preprocess data (remove empty lines, convert to floats)
  data = [float(line.strip()) for line in data if line.strip()]

  # Choose analysis algorithm
  if algorithm == "default":
    results = {"average": sum(data) / len(data)}
  elif algorithm == "advanced":
    # Import libraries for advanced analysis (assuming not built-in)
    import statistics
    results = {
      "average": statistics.mean(data),
      "standard_deviation": statistics.stdev(data),
      "median": statistics.median(data)
    }
  else:
    raise ValueError(f"Unsupported algorithm: {algorithm}")

  return results

# Example usage
data_path = "data.txt"  # Replace with your actual data file path
analysis_results = analyze_data(data_path, algorithm="advanced")

if analysis_results:
  print("Analysis Results:")
  
  import aiohttp
import aiofiles
import asyncio
import json
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5/weather"):
        self.api_key = api_key
        self.base_url = base_url

   

    async def save_weather_data(self, city, data):
        filename = f"{city}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        async with aiofiles.open(filename, 'w') as file:
            await file.write(json.dumps(data, indent=4))
        print(f"Weather data saved to {filename}")

    def parse_weather_data(self, data):
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return f"""
        Weather: {weather_desc}
        Temperature: {temp}°C
        Feels Like: {feels_like}°C
        Humidity: {humidity}%
        Wind Speed: {wind_speed} m/s
        """

    async def get_and_save_weather(self, city):
        try:
            data = await self.fetch_weather(city)
            weather_report = self.parse_weather_data(data)
            print(f"Weather in {city}:\n{weather_report}")
            await self.save_weather_data(city, data)
        except Exception as e:
            print(f"Error fetching weather data for {city}: {e}")

async def main():
    api_key = 'your_openweathermap_api_key'  # Replace with your actual API key
    cities = ['London', 'New York', 'Tokyo', 'Sydney']

    weather_fetcher = WeatherFetcher(api_key)
    tasks = [weather_fetcher.get_and_save_weather(city) for city in cities]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

  for key, value in analysis_results.items():
    print(f"{key}: {value}")

