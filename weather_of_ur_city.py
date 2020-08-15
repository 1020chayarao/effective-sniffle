#it's simple program to find the weather details of any city using openweathermap api

import requests,json

api_key="you_api_key"
base_url="http://api.openweathermap.org/data/2.5/weather?"

city_name=input("enter your city name:")

full_url=base_url + "appid=" +api_key +"&q="+city_name

response=requests.get(full_url)

x=response.json()

if x['cod']!="404":
    y=x["main"]
    current_temperature=y["temp"]
    current_pressure=y["pressure"]
    current_humidity=y["humidity"]
    z=x["weather"]
    weather_description=z[0]["description"]
    print("Temperature(in kelvin unit) ="+ str(current_temperature )+
          "\nAtmosperic pressure (in hPa unit) =" +str(current_pressure) +
          "\nHumidity (in percentage) =" +str(current_humidity) +
          "\nDescription =" + str(weather_description))
else:
    print("Ooops! Your city not found  :(")
