

import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com/"


response = requests.get(URL)

response.raise_for_status()

document = BeautifulSoup(response.text)

for element in document.find_all("div", "quote"):
    print(element.text)
    break
