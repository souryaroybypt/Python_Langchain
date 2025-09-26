import requests
import json

resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current=temperature_2m,relative_humidity_2m')

url = 'https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current=temperature_2m,relative_humidity_2m'


print("Status:", resp.status_code)
print("Response JSON:", resp.json())

res = resp.json();

try:
    resp = requests.get(url,timeout=10)
    resp.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error during request:",e)
else:
    try:
        res = resp.json()
        print("Status:",resp.status_code)
        print("Response JSON:",res)

        with open("weather.json","w") as f:
            json.dump(res,f)
        
        print("Response saved to weather.json")
    
        for key,val in res.items():
            print(key,":",val)
    except:
        print("Failed to parse JSON:")
