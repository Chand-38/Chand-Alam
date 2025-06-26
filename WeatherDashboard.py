import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Step 1: Configuration
API_KEY = 'YOUR_API_KEY'  # Replace with your actual key
CITY = 'Delhi'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Step 2: Fetch Data
response = requests.get(URL)
data = response.json()

# Step 3: Extract and Organize Data
dates = []
temps = []
humidities = []

for entry in data['list']:
    dt_txt = entry['dt_txt']
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']

    dates.append(datetime.datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
    temps.append(temp)
    humidities.append(humidity)

# Step 4: Plotting Temperature
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, color='orange')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Plotting Humidity
plt.figure(figsize=(12, 6))
sns.barplot(x=dates, y=humidities, palette='Blues_d')
plt.title(f"5-Day Humidity Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
