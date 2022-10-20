rep = input("Hey how's it going? ")

while rep != "stop copying me".casefold():
	print(rep)
	rep = input()

if rep == "stop copying me":
	print("UGH FINE YOU WIN")