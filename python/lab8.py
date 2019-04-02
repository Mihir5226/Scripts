from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.theverge.com/").content
soup=BeautifulSoup(data,'html.parser')

news_list=soup.findAll("h2", {"class":"c-entry-box--compact__title"})

  
for news in news_list:
 print (news.text)
 print("*"*75)

