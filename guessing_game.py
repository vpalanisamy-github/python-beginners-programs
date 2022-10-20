import random
guess_number = int(input("Guess a number between 1 and 10: "))
rand_number = random.randint(1, 10)

while guess_number == True:
	if guess_number < rand_number:
        print("Too low, try again!")
        guess_number = int(input("Guess a number between 1 and 10: "))
    elif guess_number > rand_number:
        print("Too high, try again!")
        guess_number = int(input("Guess a number between 1 and 10: "))
    elif guess_number == rand_number:
        print("You guessed it! You won!")
        play_again = input("Do you want to keep playing?")
        if play_again == 'y':
            guess_number = int(input("Guess a number between 1 and 10: "))
            rand_number = random.randint(1, 10)
        elif play_again == 'n':
            print("Thanks for playing! Bye.")
            break
    else:
        print("something went wrong.")
        break


print(f"The random number is {rand_number}")
