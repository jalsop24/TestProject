
import requests


URL = "https://automatetheboringstuff.com/files/rj.txt"

response = requests.get(URL)

print(response.text[:150])
print(response.content[:150])
print(response.headers)
print(response.status_code)
