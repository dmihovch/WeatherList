from creds import weather_key
import requests

city_name = input("Enter your city/town name:\n")
state_code = input("Enter your two character state code:\n")
country_code = input("Enter your two character country code:\n")

lat_lon_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={weather_key}'

lat_lon = requests.get(lat_lon_url).json()

lat = lat_lon[0]['lat']
lon = lat_lon[0]['lon']

current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}'

current_weather = requests.get(current_weather_url).json()

weather = current_weather['weather'][0]['description']
temp_kelvin = current_weather['main']['temp']
temp_far = ((int(temp_kelvin) - 273) * (9/5)) + 32

print(weather)
print(temp_far)
