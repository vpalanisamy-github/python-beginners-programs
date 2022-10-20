import requests
import random

url = "https://icanhazdadjoke.com/search"

user_input = input("Let me tell you a joke! Give me a topic: ")


response = requests.get(url, 
	headers={"Accept": "application/json"},
	params = {"term": user_input}
	)

data = response.json()
result = data["results"]

if len(result):
	joke = (random.choice(result))["joke"]
	print(f"I've got {len(result)} joke(s) about {user_input}. Here's one:")
	print(joke)

else:
	print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")


# print(len(result)) #picks cat searched jokes results and prints

