# A leap year is exactly divisible by 4 except for century years (years ending with 00). 
# The century year is a leap year only if it is perfectly divisible by 400.


year = int(input("which year do you want to check?\n"))

if year%4 == 0:
	if year%400 == 0:
		print(f"{year} is a leap year")
	elif year%100 == 0:
		print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")

#Another solution

if year%4 == 0:
	if year%100 == 0:
		if year%400 == 0:
			print("Leap year")
		else:
			print("Not a leap year")
	else:
		print("Leap year.")
else:
	print("Not a leap year.")