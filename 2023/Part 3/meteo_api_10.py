import requests
from datetime import datetime
from time import strftime, mktime

# api endpoint and access key
URL = "https://api.stormglass.io/v2/weather/point"
API_KEY = "80f07db0-9c8e-11ed-bce5-0242ac130002-80f07e50-9c8e-11ed-bce5-0242ac130002"
"""
ahmedazongnimon : 5d337b54-9c3c-11ed-b59d-0242ac130002-5d337bcc-9c3c-11ed-b59d-0242ac130002
ahmedaonn : 80f07db0-9c8e-11ed-bce5-0242ac130002-80f07e50-9c8e-11ed-bce5-0242ac130002
"""

# Récupère l'année, le mois, le jour et l'heure actuel
year = int(strftime("%Y"))
month = int(strftime("%m"))
day = int(strftime("%d"))
hour = int(strftime("%H")) 

# Convertion de la date et l'heure dans un format Unix utilisable par l'API
# Pour plus d'info : https://www.unixtimestamp.com/
start_dateTime = datetime(year, month, day, hour) # 2023-01-25 17:00:00
start_unix_timestamp = int(mktime(start_dateTime.timetuple())) # 1674666000
end_unix_timestamp = start_unix_timestamp+86400*7 # 1675270800 = 1674666000 + nb de secs dans 1 jour * 7

PARAMS = {
    'lat': 12.636006095666911,
    'lng': -7.996213675879031,
    'start': start_unix_timestamp,
    'end': end_unix_timestamp,
    'params': ','.join(['windSpeed', 'precipitation', 'humidity', 'cloudCover', 'airTemperature', 'pressure'])
    }

""" pertinents params :
airTemperature : Air temperature in °C | cloudCover : Total cloud coverage in % | humidity : Relative humidity in % |
pressure : Air pressure in hPa | precipitation : Mean precipitation in kg/m²/h = mm/h |
windSpeed : Speed of wind at 10m above sea level in m/s
"""

r = requests.get(url = URL, params = PARAMS, headers={'Authorization' : API_KEY})
print(r.url, "\n")

json_data = r.json()

with open(mode="w", file=r"C:\Users\HP\Documents\Files\scripts\Python codes\meteo_res\weather_stromglass.txt") as file:
    file.write(str(json_data))
    file.close()

heure = 0 #int(str(strftime("%H")).replace("0", ""))
time = json_data['hours'][heure]['time']
airTemperature = json_data['hours'][heure]['airTemperature']['sg']
cloudCover = json_data['hours'][heure]['cloudCover']['sg']
humidity = json_data['hours'][heure]['humidity']['sg']
precipitation = json_data['hours'][heure]['precipitation']['sg']
windSpeed = json_data['hours'][heure]['windSpeed']['sg']
pressure = json_data['hours'][heure]['pressure']['sg']

weather_info = {
        'Time' : str(time).replace("T", " ")[0:-9],
        'Air Temperature' : str(airTemperature) + "°C",
        'Cloud Cover' : str(cloudCover) + "%",
        'Humidity' : str(humidity) + "%",
        'Precipitation' : str(precipitation) + "mm/h",
        'Wind Speed' : str(windSpeed) + "m/s",
        'Pressure' : str(pressure) + "hPa"
        }

for param in weather_info:
    print(param, ':', weather_info[param])



# Résultat à 08h
"""
Time : 2023-01-25 18:00
Air Temperature : 35.52°C
Cloud Cover : 66.1%
Humidity : 13.9%
Precipitation : 0.0mm/h
Wind Speed : 2.54m/s
Pressure : 1006.27hPa
https://api.stormglass.io/v2/weather/point?lat=12.636006095666911&lng=-7.996213675879031&start=1674669600&end=1675274400&params=windSpeed%2Cprecipitation%2Chumidity%2CcloudCover%2CairTemperature%2Cpressure
"""     