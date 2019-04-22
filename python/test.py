import json 
import requests
import panda as pd

r = requests.get('http://localhost:3000/')

data =r.json()

df=pd.read_json(r,orient='columns')
df.head(10)

#pop = input("Enter state")

#if(pop=="Alabama"):
   # print(data[0]['States '] + " " +"is" + " "+ data[0]['Population Estimates'])
#print(data)





#print(data[1]['name'] + " " +"is" + " "+ data[1]['color'])
#print(data[2]['name'] + " " +"is" + " "+ data[2]['color'])
#print(data[3]['name'] + " " +"is" + " "+ data[3]['color'])