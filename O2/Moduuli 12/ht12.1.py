import requests
import json
url = "https://api.chucknorris.io/jokes/random"
try:
    req = requests.get(url)
    if req.status_code == 200:
        print(req.json()["value"])
        # print(json.dumps(req.json(), indent=2))
    else:
        print("Hakua ei voitu suorittaa.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
