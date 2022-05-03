import requests

location_data = requests.get("http://ip-api.com/json/").json()
city = location_data["city"]
# replace the api key with your api key
api_key = "??" 
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
data_weather = requests.get(url).json()
temp = data_weather["main"]["temp"] - 273.15
condition = data_weather["weather"][0]["description"]
print(f"temperature: {temp:.1f}, city: {city}, condition: {condition}")
