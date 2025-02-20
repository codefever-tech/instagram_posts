import requests

url = "https://official-joke-api.appspot.com/random_joke"

joke = requests.get(url).json()
print(f"{joke['setup']}")
print(f" - {joke['punchline']}")
