import json 
import requests

#print('please enter your zip code:')
#zip =(input)

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=12345,us&appid=7301e48b81a0ecdc32f45af58909060e')

data =r.json()

print(type(data['weather'][0]['description']))
print(data['weather'][0]['description'])