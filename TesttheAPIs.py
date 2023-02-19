import requests

response = requests.get("https://random-word-api.herokuapp.com/word")

print(response)