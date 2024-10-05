import datetime as dt
import requests
API_KEY = "Your API"

# Getting user city as a input
user_input = input("Enter a city : ")

#Request weather data
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=<Your API>&units=metric")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    feels_like = round(weather_data.json()['main']['feels_like'])
    wind_speed = weather_data.json()['wind']['speed']
    humidity = weather_data.json()['main']['humidity']
    sunrise = dt.datetime.fromtimestamp(weather_data.json()['sys']['sunrise'])
    sunset = dt.datetime.fromtimestamp(weather_data.json()['sys']['sunset'])
     
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
    print(f"It feels like {feels_like}°F in {user_input}")
    print(f"The wind speed in {user_input} is: {wind_speed} mph")
    print(f"The humidity in {user_input} is: {humidity}%")
    print(f"The sunrise in {user_input} is: {sunrise}")
    print(f"The sunset in {user_input} is: {sunset}")
    print(f"The latitude in {user_input} is: {weather_data.json()['coord']['lat']}")
    print(f"The longitude in {user_input} is: {weather_data.json()['coord']['lon']}")

    file_name = f"{user_input}_weather_data.txt"
    with open(file_name, "w") as file:
        file.write(f"The weather in {user_input} is: {weather}\n")
        file.write(f"The temperature in {user_input} is: {temp}°F\n")
        file.write(f"It feels like {feels_like}°F in {user_input}\n")
        file.write(f"The wind speed in {user_input} is: {wind_speed} mph\n")
        file.write(f"The humidity in {user_input} is: {humidity}%\n")
        file.write(f"The sunrise in {user_input} is: {sunrise}\n")
        file.write(f"The sunset in {user_input} is: {sunset}\n")
        file.write(f"The latitude in {user_input} is: {weather_data.json()['coord']['lat']}\n")
        file.write(f"The longitude in {user_input} is: {weather_data.json()['coord']['lon']}\n")
        file.close()
    
    print(f"Weather data for {user_input} has been saved to {file_name}")
    print("Thank you for using the weather app!")
