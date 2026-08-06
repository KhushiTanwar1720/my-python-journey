import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    current = data["current_condition"][0]

    print(f"\n:🌤️  Weather in {city.title()}")
    print("-" * 30)
    print("🌡️ Temperature :", current["temp_C"], "°C")
    print("🥵 Feels Like  :", current["FeelsLikeC"], "°C")
    print("☁️ Condition   :", current["weatherDesc"][0]["value"])
    print("💧 Humidity    :", current["humidity"], "%")
    print("💨 Wind Speed  :", current["windspeedKmph"], "km/h")

else:
    print("Could not fetch weather data.")