import requests

#global apikey for using weather api
apikey = '512bc4e1c263f4c268067dd26b707ac7'

def show_weather(current_user):
    """
    shows the weather at the location of the given user
    current_user is user obj with 4 attributes
    .name
    .city
    .lat
    .lon
    lat and lon will be used for weather information 
    """
    lat = current_user._lat
    lon = current_user._lon
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&APPID={}'.format(lat,lon, apikey))

    json_data = response.json()

    weather_desc = json_data['weather'][0]['description'].capitalize()
    current_temp = str(json_data['main']['temp'])
    degree_sign = u'\N{DEGREE SIGN}'
    print('In {}, {}, here is the following weather information: '.format(current_user._city, current_user._count.upper()))
    dis = "The weather condition: {}. The current temp: {} ".format(weather_desc, current_temp) + degree_sign + "C"
    print(dis)