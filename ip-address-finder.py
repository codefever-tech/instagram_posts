import requests

res = requests.get('https://ipinfo.io')
data = res.json()
print(f"IP: {data['ip']}\nCity: {data['city']}, {data['region']}")
