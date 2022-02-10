
import requests

URL = "https://webhook.site/60bf3e6b-9ab7-4607-9303-1db0598d2990"

headers = {
    "user-agent": "python-test/requests",
    "api-token": "some_random_string"
}

payload = {
    "data": {
        "a": 1,
        "b": 2
    },
    "id": 34
}

response = requests.post(URL, headers=headers, json=payload)

print(response.text[:150])
print(response.content[:150])
print(response.headers)
print(response.status_code)

