from os import system, name


# define our clear function for terminal clearing
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')


symbol = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         
                       .-------------.
                      /_______________\\
'''


#Printing the symbol to represent the auction
print(symbol)

#Greetings
print("Welcome to the secret auction program")
bidders = {}
winner = ''


#highest bidder for the auction
def highest_bid_find(bidders):
	high_bid = 0
	for key in bidders:
		if bidders[key] >= high_bid:
			winner = key
			high_bid = bidders[key]
	clear()
	print(f"The winner is {winner} with bid of ${bidders[winner]}. ")
	


#Auction bidding process
while True:
	key = input("what is your name?: ")
	value = int(input("What's your bid?: $"))

	bidders[key] = value

	new_member = input("Are there any other bidders? Type 'yes' or 'no'.")
	if new_member == 'yes':
		clear()
	elif new_member == 'no':
		highest_bid_find(bidders)
		break
	else:
		print("Wrong Input")
		highest_bid_find(bidders)
		break











