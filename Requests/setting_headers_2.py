
import requests

URL = "http://furnish-labelling.herokuapp.com/api/projects/"

headers = {
    "Authorization": "Token 40a9bd366f6b905f541e51cc92dbd67b5e93c91c",
}

response = requests.get(URL, headers=headers, params={"page": 1, "page_size": 5})

projects = response.json()

# print(response.text[:150])

print(projects["count"])

for project in projects["results"]:
    print(project["title"])

print(response.headers)
print(response.status_code)