# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:09:07 2020

@author: Dawson
"""

import requests
import key

def getWeather():  
    # Enter your API key here 
    api_key = key.getKey()
      
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name 
    zipCode = "08021"
      
    # complete_url variable to store 
    # complete url address 
    complete_url = (base_url + "zip=" + zipCode + "&appid=" + api_key)
      
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
      
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
      
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
      
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
      
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
      
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
      
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
      
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
      
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
      
        current_temp = int(current_temperature*(9/5)-459.67)
        # print following values 
        weatherData = ("Here is your weather forecast for today," +
                       "\n Temperature is " +
                        str(current_temp) + ' degrees Farenheit,' + 
              "\n humidity is " +
                        str(current_humidiy)+' Percent,' +
              "\n weather outside can be described as " +
                        str(weather_description)) +',' + "\n"
      
        #fmanager.openNuggetFile()
        #fmanager.appendNuggetFile(weatherData)
        print(weatherData)
        print('weather data gathered')
        return weatherData
    else: 
        weatherData = ('Weather Data could not be gathered')
        print(" City Not Found ") 
        return weatherData
        
#getWeather()