import random

name = input("What is your name? ")

print("Welcome to The Number Guessing Game! ")

high_score = []


all_scores = []

start = input(f"Do you want to start the game {name}? (Y/N) ")

while start.title() == "Yes" or start.upper() == "Y":
  NUMBER = random.randint(1, 10)
  attempt = 0
  
  
  def guess_number():
    while True:
      try:
        guess = input("Guess a number which you think I might have chosen between 1 and 10. ")
        guess = int(guess)
        break
      except ValueError:
        print("Sorry! That's not a number.")
    return guess
    
  guess = guess_number()
  attempt += 1
  
  while guess != NUMBER:
    attempt += 1

    if guess > 10 or guess < 1:
      print("Number must be in the range of 1 and 10.")
      guess = guess_number()
    
    elif guess > NUMBER:
      print("No, It's not that high. It's lower.")
      guess = guess_number()

    elif guess < NUMBER:
      print("No, it's not that low. It's higher.")
      guess = guess_number()

  all_scores.append(attempt)
  high_score = min(all_scores)

  print(f"You got it! You guessed it right {name}. The number is {NUMBER}")
  print(f"Attempts you took(Your Score): {attempt}")
  print("GAME OVER!")

  start = input("Do you want to play again? (Y/N) ")
  print(f"Best Score: {high_score}")
  continue

print(f"Thank you for showing interest in the game {name}!")
