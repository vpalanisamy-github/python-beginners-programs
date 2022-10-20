import requests

url = "http://www.google.com"
response = requests.get(url)

print(f" Your request to {url} has came back with the status code of {response.status_code}")