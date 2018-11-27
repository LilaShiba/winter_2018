import json, requests

############################### API Request Parameters #########################################################################
def url():
    api_token = '31df5488194dc5669a4d8c1b5800ef60'
    lat = '40.7128'
    lon = '-74.0060'
    url = 'https://api.darksky.net/forecast/'+api_token+'/'+lat+','+lon
    data = requests.get(url).json()
    return data
############################### Make API Call #########################################################################
def parse_call(data):
    current = data['currently']
    #summary = current['summary']
    temp = current['temperature']
    #wind = current['windSpeed']
    #uv = current['uvIndex']
    #min_cast = data['minutely']['data'][0]
    #min_sum = data['minutely']['summary']
    #daily = data['daily']['data'][0]
    #moon = daily['moonPhase']
    return temp
############################### Make API Call #########################################################################
