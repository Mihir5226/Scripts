from bs4 import BeautifulSoup
import requests, re
r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup(r,"lxml")
print(type(r))
print(type(soup))

#class 'bs4.BeautifulSoup'
#print(soup.prettify()[:100])
#for link in soup.find_all('a'): print(link.get('href'))

for link in soup.find_all('a',attrs={'href':re.compile("^https://github.com")}):
    print(link.get('href'))
