#Weather CLI App 
import requests
import datetime

API_KEY = "d4e6cd61ef46661abd2d747a99eba5af"

def get_weather_emoji(description):
    if "clear" in description:
        return "☀️"
    elif "clouds" in description:
        return "☁️"
    elif "overcast" in description:
        return "☁️☁️"
    elif "rain" in description:
        return "🌧️"
    elif "thunderstorm" in description:
        return "⛈️"
    elif "snow" in description:
        return "❄️"
    else:
        return "🌫️"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    city = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    emoji = get_weather_emoji(description)
    wind_speed = data["wind"]["speed"]
    print(f"\n==== Weather in {city} ====")
    print(f"Conditions: {description} {emoji}")
    print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s \n")
    timestamp = data["dt"]
    UTC_offset_seconds = data["timezone"]
    UCT_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
    offset_hours = UTC_offset_seconds / 3600
    timezone_offset = datetime.timedelta(seconds=UTC_offset_seconds)
    current_time = datetime.datetime.fromtimestamp(timestamp)
    local_time = UCT_time + timezone_offset
    formatted_time = local_time.strftime("%d %B, %Y %H:%M")
    if offset_hours >= 0:
        tz_string = f"GMT+{int(offset_hours)}"
    else:
        tz_string = f"GMT-{int(offset_hours)}"
    print(f"{formatted_time}, {tz_string}")

def main():
    while True:
    #Menu System
        #Option to check weather
        #Option to exit
        print("Weather App")
        print("1. View the weather")
        print("2. Exit \n")

        choice = input("Please input an option: \n")

        if choice == "1":
            city = input("Enter city name: \n")
            weather = get_weather(city)
            if weather["cod"] == 200:
                display_weather(weather)
            else:
                print("City not found! \n")
                break
        else:
            print("Goodbye!\n")

main()




