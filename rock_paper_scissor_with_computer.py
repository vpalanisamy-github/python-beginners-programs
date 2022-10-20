import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("...rock...\n...paper...\n...scissors...\n")
winning_score = int(input("Choose your winning score."))
player_wins = 0
computer_wins = 0


# Your's ASCII art choice:
while (player_wins < winning_score) and (computer_wins < winning_score):
    player1 = input("Enter your input: ")
    random_number = random.randint(0, 2)
    computer = None

    # Your's ASCII art choice:
    if player1 == 'rock':
        print(rock)
    elif player1 == 'paper':
        print(paper)
    elif player1 == 'scissors':
        print(scissors)
    else:
        print("Please give any of the given input.")

    print(f"Your choice: {player1}\n")

    # computer's ASCII art choice:
    if random_number == 0:
        computer = 'rock'
        print(rock)
    if random_number == 1:
        computer = 'paper'
        print(paper)
    if random_number == 2:
        computer = 'scissors'
        print(scissors)

    print("The Computer plays: " + computer)

    # condition check
    if player1 == computer:
        print("It's a tie")

    elif player1 == "rock":
        if computer == 'paper':
            computer_wins += 1
            print("SHOOT! \nComputer wins")
        elif computer == 'scissors':
            player_wins += 1
            print("Yay! \nYou win")

    elif player1 == "paper":
        if computer == 'scissors':
            computer_wins += 1
            print("SHOOT! \nComputer wins")
        elif computer == 'rock':
            player_wins += 1
            print("Yay! \nYou win")

    elif player1 == "scissors":
        if computer == 'rock':
            computer_wins += 1
            print("SHOOT! \nComputer wins")
        elif computer == 'paper':
            player_wins += 1
            print("Yay! \nYou win")

    # To avoid final y or n asking(it breaks loop if final score reached)
    if winning_score == player_wins or winning_score == computer_wins:
        break

    # Check for the next play.
    play_again = input("Want to play again? 'y' or 'n':   ")
    if play_again == 'y':
        continue
    elif play_again == 'n':
        print("Thank you for playing!")
        break
    elif play_again == 'q':
        print("You are quitting....")
        break
    else:
        print("Wrong input.")
        break

print(
    f"FINAL SCORE: \nPlayer Score: {player_wins} \nComputer Score: {computer_wins}")
