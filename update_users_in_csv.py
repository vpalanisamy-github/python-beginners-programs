

from csv import reader, writer


# Create csv file.

with open("userss.csv", "w") as file:
	new_file = writer(file)
	new_file.writerow(["First Name", "Last Name"])
	new_file.writerow(["Colt", "Steele"])
	new_file.writerow(["Grace", "Hopper"])
	new_file.writerow(["Alan", "Turing"])
	new_file.writerow(["Colt", "Steele"])


def update_users(old_first, old_last, new_first, new_last):
	count = 0
	with open("users.csv", 'r') as file:
		csv_file = reader(file)
		file_list = list(csv_file)
	with open("users.csv", 'w') as file:
		csv_file = writer(file)
		for row in file_list:
			if row == [old_first, old_last]:
				count+=1
				mod_list = [new_first, new_last]
				csv_file.writerow(mod_list)
			else:
				csv_file.writerow(row)
	# csv_file.truncate()s
	return "Users updated: {}.".format(count)


print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.


