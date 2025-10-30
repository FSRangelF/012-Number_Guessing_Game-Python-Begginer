import art
import random

def num_of_attempts():
  """return the number of attempts based in the selected level"""
  option = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  while option != "easy" and option != "hard":
    option = input("This is not a valid option.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
  if option == "easy":
    return 10
  else:
    return 5

def compare_number(num1, num2):
  """return the result of a number comparision and print the relative direction of the guess"""
  if num1 == num2:
    print(f"You got it! The answer was {num2}.")
    return True
  elif num1 > num2:
    print("Too High\n Guess Again.")
    return False
  elif num1 < num2:
    print("Too Low.\n Guess Again.")
    return False

max = 100
min = 1
target = random.randint(min, max)
print(art.logo)
print(f"I´m thinkink of a number between {min} and {max}.")
attempts = num_of_attempts()
win = False
while attempts > 0 and not win:
  print(f"You have {attempts} remaining to guess the number")
  guess = int(input("Make a guess: "))
  win = compare_number(num1=guess, num2=target)
  attempts -= 1
  if attempts == 0:
    print(f"You Lose! The number was {target}")
    
