#WeatherApp.py
#Name:
#Date:
#Assignment:

import WeatherInfo
from WeatherInfo import setCity

#Set your key
WeatherInfo.setKey("d877ca2ccc179e10caa55e272b5caa8b")

#Ask the user for their city
city = input("What city: ")
setCity(city)
#Update the weather with the given city
WeatherInfo.updateWeather()
print(str(round(((WeatherInfo.getTemp()-273)*9/5)+32))+" degrees F")
#Request any data you need from the WeatherInfo API

#This is a change

#Process the data
#convert temperature to fahrenheit,
#determine wind speed in words
#decide jacket and umbrella status

#Report to the user the weather of their city

#Ask user if they would like another weather report
#If yes, loop to the top of your program where they are asked for a city.
#If no, end with a goodbye statement of some sort.
