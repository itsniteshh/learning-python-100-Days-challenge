from art import logo, vs
from game_data import data
#from replit import clear
import random


def format_data(account):
  #formatting the random account to be readable
  account_name = account["name"]
  account_des = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_des}, from {account_country}")


#using if statement to check if user is correct or not
def check_answer(user_guess, a_followers, b_followers):
  """takes user guess and follow account of a and b and returns answer"""
  if a_followers > b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

#display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#repeating the game questions
while game_should_continue:

  #generate a random account from the data
  #making acount b turn into account a after every correct guess
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  #asking user for a guess
  user_guess = input("who has more followers? Type 'A' or 'B': ").lower()


  #checking if user guess is corrrect
  #get follower count
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]
  is_correct = check_answer(user_guess, a_followers, b_followers)

  # clearing the screen after the end of rounds
  clear()
  print(logo)


  #user feedback
  #score keeping
  if is_correct:
    print(f"You're right! Current Score: {score}")
    score += 1
  else:
    print(f"Sorry, that's wrong answer. Final score: {score}")
    game_should_continue = False








