
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.player_reply = input("Welcome to BlackJack. Do you want to play a game? Type 'y'or 'n':\n")


import os

def play():
	card_value = [11,2,3,4,5,6,7,8,9,10,10,10,10]

	import random
	my_card = [random.choice(card_value), random.choice(card_value)]
	dealer_card = [random.choice(card_value),random.choice(card_value)]

	my_hand = sum(my_card)
	dealer_hand = sum(dealer_card)


	while int(sum(dealer_card)) < 17:
		dealer_card.append(random.choice(card_value)) #append helps to add list values inside the list and extend helps to add list inside list
		dealer_hand = sum(dealer_card)


	os.system('cls')
	print("Your card: {} , current score: {}".format(my_card, my_hand))
	print("Computer's first card: {}".format(dealer_card[0]))


	iscontinue = 1
	while iscontinue == 1:
		while sum(my_card) < 21:
			anothercard = input("Type 'y' to get another card, type 'n' to pass: \n")
			if anothercard == 'y':
				my_card.append(random.choice(card_value))
				my_hand = sum(my_card)
				print("Your card: {} , current score: {}".format(my_card, my_hand))
			elif anothercard == 'n':
				print("Your card: {} , current score: {}".format(my_card, my_hand))
				break
		iscontinue = 0



	# print(my_card, dealer_card,my_hand , dealer_hand) #Checking purpose

	if dealer_hand == my_hand:
		print("Your final hand: {},  Final score: {} \nComputer's final hand: {}, Final score: {} \n Same Score. Draw....!".format(my_card,my_hand,dealer_card,dealer_hand))
	elif dealer_hand > my_hand and dealer_hand<=21:
		print("Your final hand: {},  Final score: {} \nComputer's final hand: {}, Final score: {} \n  You went low..You lose....".format(my_card,my_hand,dealer_card,dealer_hand))
	elif my_hand>21:
		print("Your final hand: {},  Final score: {} \nComputer's final hand: {}, Final score: {} \n You went out..You lose....".format(my_card,my_hand,dealer_card,dealer_hand))
	else:
		print("Your final hand: {},  Final score: {} \nComputer's final hand: {}, Final score: {} \n Congratulations. You Win....!".format(my_card,my_hand,dealer_card,dealer_hand))



game_start = input("Welcome to BlackJack. Do you want to play a game? Type 'y'or 'n': \n")
if game_start == 'y':
	play()

isplay = 1
while isplay == 1:
	play_again = input("Do you want to play again? Type 'y'or 'n': \n")
	if play_again == 'y':
		play()
	else:
		os.system('cls')
		print('Thank you for playing..!')
		isplay = 0