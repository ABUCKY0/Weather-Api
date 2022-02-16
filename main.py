########################################################################
# Filename    : main.py
# Description : print weather to console from OPENWEATHERMAP.ORG
# Author      : Aaron Buckner
# modification: 2021/02/04
########################################################################

from requests import get
import json
import time
import os
api = ${{ secrets.SuperSecret }}
weather_api = 'https://pro.openweathermap.org/data/2.5/weather?lat=29.973330&lon=-95.687332&appid='+api'&units=imperial'
one_call_api = 'https://pro.openweathermap.org/data/2.5/onecall?lat=29.973330&lon=-95.687332&appid='+api'&units=imperial'


def degrees_to_cardinal(d):
    '''
    note: this is highly approximate...
    '''
    dirs = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW",
        "WSW", "W", "WNW", "NW", "NNW"
    ]
    ix = int((d + 11.25) / 22.5)
    return dirs[ix % 16]


while True:
    result = get(one_call_api).json()
    degrees = result['current']['wind_deg']
    wind_gust = result.get('current').get('wind_gust')
    weather_temp = result['current']["temp"]
    url = weather_api
    wind_speed = result["current"]["wind_speed"]
    pressure = result['current']['pressure']
    feels_like = result['current']["feels_like"]
    uvi = result.get('current')
    uvi = uvi.get('uvi')
    current_data = result.get('current')
    current_data = current_data.get('weather')
    conditions_data = json.dumps(current_data)
    conditions_data = conditions_data.replace('"description": ', "")
    conditions_data = conditions_data.replace('"', "")
    conditions = conditions_data.split(", ")
    atmo_pressure = result.get('current').get('pressure')
    humidity = result.get('current').get('humidity')
    dew_pt = result.get('current').get('dew_point')
    wind_direction = degrees_to_cardinal(degrees)

    any_alerts = result.get('alerts')
    any_alert = json.dumps(any_alerts)
    any_alert = any_alert.replace('"event": ', "")
    any_alert = any_alert.replace('"', "")

    if any_alert != "null":
        any_alert = any_alert.split(", ")
    else:
        any_alert = [
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
            'NONE',
        ]

    print("Current Conditions: " + str(conditions[2].swapcase()))
    print("")
    print("Temp: " + str(weather_temp) + "°F")
    print("Feels Like: " + str(feels_like) + "°F")
    print("")
    print("Wind Speed: " + str(wind_speed) + " Miles per Hour ")
    print("Wind Gust: " + str(wind_gust) + " Miles per Hour ")
    print("Wind Direction: " + wind_direction)
    print('')
    print("UV Index: " + str(uvi))
    print('Dew Point: ' + str(dew_pt) + '\N{DEGREE SIGN}F')
    print('Atmosperic Pressure: ' + str(atmo_pressure) + " hPa")
    print('Humidity: ' + str(humidity) + "%")
    print('')
    print("Alert Name: " + any_alert[0])
    print("Second Alert Name: " + any_alert[13])
    time.sleep(5)
    os.system('clear')

