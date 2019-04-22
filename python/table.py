#from bs4 import BeautifulSoup
#import requests, re

import urllib.request
#from urllib.requests import urlopen
import bs4 as bs

url = 'https://www.enchantedlearning.com/usa/states/population.shtml'
html=urllib.request.urlopen(url)
print(html)
#soup =bs.BeautifulSoup(html,'lxml')



#data = requests.get("https://www.enchantedlearning.com/usa/states/population.shtml").content

#soup=BeautifulSoup(data,'html.parser')

#news_list=soup.find("div", {"class":"car_inner--margins markdown"})

#print (news_list.text)
#for news in news_list:
 #print (news.text)
 #print("*"*75)