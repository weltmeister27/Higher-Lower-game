from game_data import data
import art
from random import randint
from replit import clear

is_game_continued = True

score = 0

def compare_display(a_choice, b_choice, score):
  clear()
  print(art.logo)
  if score != 0:
    print(f"You're right! Current score is {score}")
  print(f"Compare A: {a_choice['name']}, a {a_choice['description']}, from {a_choice['country']}")
  print(art.vs)
  print(f"Against B: {b_choice['name']}, a {b_choice['description']}, from {b_choice['country']}")

def compare_followers(a_choice, b_choice):
  if a_choice['follower_count'] > b_choice['follower_count']:
    return 1
  else:
    return 0

def restart_display():
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  return choice

def options_details():
  a_random = randint(1, 50)
  b_random = randint(1, 50)

  if a_random == b_random:
    a_random += 1

  return data[a_random-1], data[b_random-1]

def answered_details(a_choice, b_choice):
  b_random = randint(1, 50)
  
  return a_choice, data[b_random-1]
  
while is_game_continued:
  if score == 0:
    a_choice, b_choice = options_details()
  else:
    a_choice, b_choice = answered_details(a_choice, b_choice)
  compare_display(a_choice, b_choice, score)
  restart = restart_display()
  result = compare_followers(a_choice, b_choice)
  if result == 1 and restart == 'a':
    is_game_continued = True
    score += 1
  elif result == 1 and restart == 'b':
    is_game_continued = False
  elif result == 0 and restart == 'b':
    is_game_continued = True
    c = a_choice
    a_choice = b_choice
    score += 1
  else:
    is_game_continued = False

clear()
print(art.logo)
print(f"Sorry that's wrong. Final score: {score}")