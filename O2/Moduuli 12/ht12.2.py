import requests
city = input("Anna paikkakunnan nimi: ")
url = 'https://api.openweathermap.org/data/2.5/weather'#?q='
api_key = '%YOUR_API_KEY%'
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric',
    'lang': 'fi'}
try:
    req = requests.get(url, params=params)
    if req.status_code == 200:
        data = req.json()
        print(f"Sää paikkakunnalla {city}: {data['weather'][0]['description']}")
        print(f"Lämpötila: {data['main']['temp']:.2f}°C")
    else:
        print("Säätilan haku epäonnistui. \n[00]")
except requests.exceptions.RequestException as e:
    print("Säätilan haku epäonnistui. \n[01]")
