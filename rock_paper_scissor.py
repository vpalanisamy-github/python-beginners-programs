#title
print(".....rock.....")
print(".....paper.....")
print("...scissors......")

#playars input
player1 = (input("(enter Player 1's choice): ")).casefold()
player2 = (input("(enter Player 2's choice): ")).casefold()

#condition check
if player1 == player2:
	print("It's a tie")

elif player1 == "rock":
	if player2 == 'paper':
		print("SHOOT! \nPlayer 2 wins")
	elif player2 == 'scissors':
		print("Yay! \nPlayer 1 wins")

elif player1 == "paper":
	if player2 == 'scissors':
		print("SHOOT! \nPlayer 2 wins")
	elif player2 == 'rock':
		print("Yay! \nPlayer 1 wins")

elif player1 == "scissors":
	if player2 == 'rock':
		print("SHOOT! \nPlayer 2 wins")
	elif player2 == 'paper':
		print("Yay! \nPlayer 1 wins")
else:
	print("Wrong input")



#another logic
if player1 == 'rock' and player2 == 'scissors':
	print('player 1 wins')
elif player1 == 'rock' and player2 == 'paper':
	print('player 2 wins')
elif player1 == 'paper' and player2 == 'scissors':
	print('player 2 wins')
elif player1 == 'paper' and player2 == 'rock':
	print('player 1 wins')
elif player1 == 'scissors' and player2 == 'paper':
	print('player 1 wins')
elif player1 == 'scissors' and player2 == 'rock':
	print('player 2 wins')
elif player1 == player2:
	print('Draw')
else:
	print('Incorrect input')
