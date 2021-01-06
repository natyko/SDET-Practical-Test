 # Mars weather
import json
import requests
import pandas as pd
import webbrowser


api_nasa_mars = 'https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0'
data = requests.get(api_nasa_mars)
# print(data)
result = json.loads(data.text)
# print(result)
# print(result.keys())
# for ii, k in result:
#     print(result[ii]['AT'], result[ii]['HWS'])



# def marsweather():
#     f = r"https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
#     data = requests.get(f)
#     tt = json.loads(data.text)
#     for i in tt:
#         return tt[i]["AT"], tt[i]["HWS"]

# print(marsweather())
