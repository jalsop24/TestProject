import requests
import pandas as pd
from bs4 import BeautifulSoup


r = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(r.text)
for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("span",{"class":"text"})).text)
print(soup.get_text())

for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("small",{"class":"author"})).text)
print(soup.get_text())
