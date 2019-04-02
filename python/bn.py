from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.barnesandnoble.com/w/toys-games-pop-games-marvel-coc-king-groot/32045919?ean=0889698267076").content
soup =BeautifulSoup(data,'html.parser')
title =soup.find("h1", {"class":"pdp-header-title"})

span =soup.find("span",id="pdp-cur-price")
print("item is %s and is %s"%(title.text,span.text))