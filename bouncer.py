# ask for age
age = input("Great day!\nWhat is your age?\n")

# 18-21 wristband
# 21+ drink, normal entry
# too young,sorry
if age:
	if int(age) >= 18 and int(age) <21:
		print("You're allowed with the wristband")
	elif int(age) >= 21 and int(age) <90:
		print("Welcome to the bluewaves Bar!")
	else:
		print("You're too young. Sorry!")
else:
	print("Please enter an age!")

