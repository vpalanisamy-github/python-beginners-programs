import requests

url = "https://icanhazdadjoke.com/"
url1 = "https://icanhazdadjoke.com/"

#returns the plain text 
plain_response= requests.get(url, headers={"Accept": "text/plain"}) #test/html will generate html JS output
#returns the JSON(JavaScript Object Notation) file which is readable using python
json_response = requests.get(url1, headers={"Accept": "application/json"})


#prints the plain text
#print(plain_response.text)
 
print(json_response.json())

#printing the key value in the json
