import requests

API_KEY = "009694ab7301a549081b400c54193783"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city name : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2 )
    feels_like = data['main']['feels_like']
    temperature_min = round(data['main']['temp_min'] - 273.15, 2)
    temperature_max = round(data['main']['temp_max'] - 273.15, 2)
    sunrise_time = data['sys']['sunrise']
    sunset_time = data['sys']['sunset']
    country = data['sys']['country']

    print("Weather : ", weather) 
    print("Temperature :", temperature, "celsius")
    print("Maximum Temperature : ", temperature_min)
    print("Minimum Temperature : ", temperature_max)
    print("Sunrise : ", sunrise_time)
    print("Sunset : ", sunset_time)
    print("Country: ", country)
    
   # print(data)

else:
    print("An error occured ")