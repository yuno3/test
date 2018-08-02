import urllib.request, urllib.parse, sys
import json

try: citycode = sys.argv[1]
except: citycode = '110010' #指定しなければさいたまが表示

resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

#辞書型に変更
resp = json.loads(resp)

print("----------------------")
print(resp["title"])
print("----------------------")
print(resp["description"]["text"])

for forecast in resp['forecasts']:
    print("----------------------")
    print(forecast['dateLabel'] + " " + forecast['date'])
    print(forecast['telop'])

print("----------------------")
