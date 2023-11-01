import requests
import json

hakusana = input("Anna hakusana:")
pyyntö =  "https://api.tvmaze.com/search/shows?q=" + hakusana
'''
vastaus = requests.get(pyyntö).json()
#print(json.dumps(vastaus, indent=2))
ekaSarja = vastaus[0]
print(f'Eka sarjan nimi: {ekaSarja ["show"] ["name"]}')
print(f'Rating: {vastaus[0] ["show"] ["rating"] ["average"]}')
'''

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
    else:
        print("Hakua ei voitu suorittaa.")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")