'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


# def extract_full_name(l):
    # return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))



# print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']

def extract_full_name2(l):
	return list(" ".join(d.values()) for d in l)


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name2(names))