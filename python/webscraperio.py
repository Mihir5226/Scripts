import requests, re 
from bs4 import BeautifulSoup
r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup=BeautifulSoup(r,"lxml")
#tags = soup.findAll("a",{"href":re.compile('(allinone)')})
#for a in tags:
 #   print(a.get('href'))
tags = soup.findAll("div", {"class":re.compile('(ratings)')})
for p in tags:
    rating=p.findAll("p",{"class":"pull-right"})
    print(rating)
    print(type(rating[0]))
    print(rating[0].string)

#tags =soup.findAll("a",{"href":re.compile('[<>#%|\{\}!\\^~\[\]`/}')})
#for a in tags:
#    print(a.get('href'))