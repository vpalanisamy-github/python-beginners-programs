import requests
import random

url = "https://icanhazdadjoke.com/search"

#
response = requests.get(url, 
	headers={"Accept": "application/json"},
	params = {"term":"friends"}
	)

data = response.json()

# print(data) #picks cat searched jokes results and prints
result = data["results"]
joke = (random.choice(result))["joke"]
print(joke)