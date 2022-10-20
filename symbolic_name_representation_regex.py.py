import re
# Name parsing

def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$') #Here ?P<first> and ?P<last> is the symbolic name representation
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

parse_name("Mrs. Tilda Swinton")




#Date parsing

def parse_date(input):
    regex_date = re.compile(r'^(?P<d>[0-9]{2})[\.,/](?P<m>[0-9]{2})[\.,/](?P<y>[0-9]{4})$')
    match = regex_date.search(input)
    if match:
        return {
            "d": match.group('d'),
            "m": match.group('m'),
            "y": match.group('y')
            }
    return None


print(parse_date("11.11.2012"))
print(parse_date("10,43,3921"))
print(parse_date("11/32/1020"))
print(parse_date("11.22.103928"))