import re


def extract_phone(input):
	phone_regex = re.compile(r'\+\d\d? ?\d{10}')
	match = phone_regex.search(input)
	if match:
		return match.group()  
	return None


def extract_all_phones(input):
	phone_regex = re.compile(r'\+\d\d? ?\d{10}')
	match = phone_regex.findall(input) 
	if match:
		return match  
	return None

def is_valid_phone(input):
	phone_regex = re.compile(r'^\+\d\d? ?\d{10}\b$')
	match = phone_regex.search(input)
	if match:
		return True  
	return False

#Alternate checking
print(extract_phone("My number is +91 9042929111 and my mom's +91 9443529887"))
print(extract_phone("+91 9443598908"))
print(extract_phone("my mom's +919443528 dfkjldfkj"))
print(extract_phone("dsjfljs"))
print("\n")
print(extract_all_phones("My number is +91 9042929111 and my mom's +91 9443529887"))
print(extract_all_phones("+91 9443598908"))
print(extract_all_phones("my mom's +919443528 dfkjldfkj"))
print(extract_all_phones("dsjfljs"))
print("\n")
print(is_valid_phone("+91 2934328742"))
print(is_valid_phone("+91 39034830983 dsfjdslfj"))
print(is_valid_phone("Hi this is my number +91 2934328742"))
print(is_valid_phone("dsjfld+91 39034830983 dsfjdslfj"))