import os.path, time
import os
import ast
import requests
import time

abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

def weather():
    try:
        # api endpoint and access key
        """ URL Format Examples
        api.openweathermap.org/data/2.5/weather?q=London,uk&appid=45db8d916b2d3e08d85801c9e0e62c00
        https://api.openweathermap.org/data/2.5/weather?appid=45db8d916b2d3e08d85801c9e0e62c00&lat=12.636006095666911&lon=-7.996213675879031
        """

        URL = "https://api.openweathermap.org/data/2.5/weather?q=Bamako&appid=45db8d916b2d3e08d85801c9e0e62c00"
        PARAMS = {
            'lat': 12.636006095666911,
            'lon': -7.996213675879031,
            'exclude': ','.join(['minutely', 'hourly', 'daily', 'alerts']),
            'lang': 'fr',
            'units': 'metric'
            }

        r = requests.get(url = URL, params = PARAMS)
        json_data = r.json()

        with open(mode="w", file=fr"C:\Users\HP\Documents\Files\scripts\Python codes\meteo_res\weather_openweather.txt") as file:
            file.write(str(json_data))
            file.close()

        networkState = True

    except Exception:
        print("\nConnectez-vous pour mettre à jour les données météorologiques.\n"
              "En attendant, voici les données la dernière session.")
        
        networkState = False
        
    with open(mode="r", file=fr"C:\Users\HP\Documents\Files\scripts\Python codes\meteo_res\weather_openweather.txt") as file:
        data = file.read()
        file.close()

    json_data = ast.literal_eval(data)
    try:
        precipitation = json_data['rain']['3h']
    except Exception:
        precipitation = 0

    try:
        if json_data['sys']['sunrise'] < time.time() < json_data['sys']['sunset']:
            moment = 'day'
        else:
            moment = 'night'
    except Exception:
        moment = 'day'
    
    return {
            'Ville' : "%s, %s (%s, %s)"%(json_data['name'], json_data['sys']['country'], json_data['coord']['lat'], json_data['coord']['lon']),
            'Temps' : str(json_data['weather'][0]['description']).capitalize(),
            'Température' : str(json_data['main']['temp']) + "°C",
            'Humidité' : str(json_data['main']['humidity']) + "%",
            'Précipitation' : str(precipitation) + "mm/h",
            'Couverture nuageuse' : str(json_data['clouds']['all']) + "%",
            'Pression atmos.' : str(json_data['main']['pressure']) + "hPa",
            'Vents' : str(round(json_data['wind']['speed']*3.6)) + "km/h / " + str(json_data['wind']['deg']) + "°",
            'Dernière mesure' : time.ctime(json_data['dt']),
            'Moment': moment,
            'Illustration': str(json_data['weather'][0]['icon']),
            'Online': networkState
            }

weather_info = weather()
print()
for param in weather_info:
    print(param, ':', weather_info[param])
        
