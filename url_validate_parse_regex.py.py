import re

url_regex = re.compile(r'((https?)://)((www\.)?[A-za-z-]{2,256}\.[a-z]{2,6})([a-zA-Z0-9@:%._\\+~#?&//=-]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
#start with 1 to call the first element
print(f"Protocol: {match.group(1)}")
print(f"https or http: {match.group(2)}") #subgroup
print(f"Domain: {match.group(3)}")
print(f"If www presents: {match.group(4)}") #subgroup
print(f"Everything Else: {match.group(5)}")
print(match.groups()) #returns tuple value sets
print(match.group()) #returns full searched string

