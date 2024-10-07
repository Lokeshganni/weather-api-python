import requests

api_key = '35ddcd48136b4335ae832158240710'

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Hyderabad"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Location: {data['location']['name']}")
    print(f"Temperature (°C): {data['current']['temp_c']}")
    print(f"Condition: {data['current']['condition']['text']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
