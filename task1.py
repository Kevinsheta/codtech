import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
API_KEY = '56a040764ae6c2ce78e6f8977355731a'  # Example key, replace with your own
CITY = 'mumbai' # Change to your desired city
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Parse data
timestamps = []
temperatures = []

for item in data['list']:
    timestamps.append(datetime.fromtimestamp(item['dt']))
    temperatures.append(item['main']['temp'])

# Visualization
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, marker='o', linestyle='-')
plt.title(f'5-Day Temperature Forecast in {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
