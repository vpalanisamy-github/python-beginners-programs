# print logos 
# select 2 random dictionary value from game_data/data dictionary which should not be same.
# compare and result high
# if high continue with 2nd data and one more random dictionary data and again these 2 should not be same
# repeat the process
# print the final score.

import os
from art import logo, vs
from game_data import data
from random import randint

def game():
  first_person = 0
  second_person = 0
  SCORE = 0
  play = 1
  
  # Chooosing the random persons for comparison
  while first_person == second_person:
    first_person = randint(0, len(data))
    second_person = randint(0, len(data))
  
  print(logo)
  while play:
  
     # Printing comparison  
    def players(first_person, second_person):
      
      print(f"Compare A: {data[first_person]['name']} , {data[first_person]['description']} , {data[first_person]['country']} ")
      print(vs)
      print(f"Against B: {data[second_person]['name']} , {data[second_person]['description']} , {data[second_person]['country']} ")
  
    players(first_person, second_person)

    
    #Comparing the players
    def playercomparison(first_person, second_person):
      if data[first_person]['follower_count'] >= data[second_person]['follower_count']:
        
        return first_person
      elif data[first_person]['follower_count'] <= data[second_person]['follower_count']:
        return second_person
    
    highscore = playercomparison(first_person, second_person)


    # Getting Input from user
    user_input = input("Who has more followers? Type 'A' or 'B': ")

    lowscore = 0
    if user_input == 'A':
      user_input = first_person
      lowscore = second_person
    elif user_input == 'B':
      user_input = second_person
      lowscore = first_person

    # Updating score and check if game continues or not
    if highscore == user_input:
      SCORE += 1
      os.system('cls')
      print(logo)
      print(f"\nYou're right! Current score: {SCORE} \n{data[highscore]['name']} has follower count of {data[highscore]['follower_count']} million. \n{data[lowscore]['name']} has follower count of {data[lowscore]['follower_count']} million")
      first_person = highscore
      second_person = randint(0, len(data))
      while second_person == first_person:
        second_person = randint(0, len(data))
    elif highscore != user_input:
      os.system('cls')
      print(logo)
      print(f"\nYou lost! Final Score: {SCORE} \n{data[highscore]['name']} has follower count of {data[highscore]['follower_count']} million. \n{data[user_input]['name']} has follower count of {data[user_input]['follower_count']} million")
      play = 0
    

  

game()




# Another Solution

# from game_data import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()

# '''

# FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

# Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

# '''



# # Generate a random account from the game data.

# # Format account data into printable format.

# # Ask user for a guess.

# # Check if user is correct.
# ## Get follower count.
# ## If Statement

# # Feedback.

# # Score Keeping.

# # Make game repeatable.

# # Make B become the next A.

# # Add art.

# # Clear screen between rounds.