logo = """

                     (    (                 )           )           *                (     
 (                   )\ ) )\ )    *   )  ( /(        ( /(         (  `      (        )\ )  
 )\ )       (   (   (()/((()/(  ` )  /(  )\()) (     )\())    (   )\))(   ( )\  (   (()/(  
(()/(       )\  )\   /(_))/(_))  ( )(_))((_)\  )\   ((_)\     )\ ((_)()\  )((_) )\   /(_)) 
 /(_))_  _ ((_)((_) (_)) (_))   (_(_())  _((_)((_)   _((_) _ ((_)(_()((_)((_)_ ((_) (_))   
(_)) __|| | | || __|/ __|/ __|  |_   _| | || || __| | \| || | | ||  \/  | | _ )| __|| _ \  
  | (_ || |_| || _| \__ \\__ \    | |   | __ || _|  | .` || |_| || |\/| | | _ \| _| |   /  
   \___| \___/ |___||___/|___/    |_|   |_||_||___| |_|\_| \___/ |_|  |_| |___/|___||_|_\  
                                                                                           
"""


from random import randint
import os
NUMBER = randint(1,101)
EASY = 10
HARD = 5


def play():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    def set_difficulty():
        if difficulty == 'hard':
            return HARD
        elif difficulty == 'easy':
            return EASY

    attempts = set_difficulty()

    while attempts !=0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        GUESS = int(input("Make a guess: "))
        attempts -=1

        if GUESS == NUMBER:
            print(f"You got it! The answer was {NUMBER}")
            break
        elif attempts == 0:
            print("You exceeded the number of attempts.You Lost..!")
            break
        elif GUESS > NUMBER:
            print("Too high \nGuess again.")
        elif GUESS < NUMBER: 
            print("Too low \nGuess again.")


    # print(f"You have {attempts} attempts remaining to guess the number")
        

while True:
    play()
    print("Thanks for playing...!")
    play_again = input("Type 'yes' if you want to play again..?: ")
    if play_again != 'yes':
        # os.system('cls')
        break
    os.system('cls')


#Another type

# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()