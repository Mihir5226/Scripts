import requests 
from bs4 import BeautifulSoup

result = requests.get("https://news.google.com/news/rss")
src= result.content
soup =BeautifulSoup(src,'html.parser')

news_list=soup.findAll("item")
for news in news_list:
  print(news.title.text)
  print("-"*60)