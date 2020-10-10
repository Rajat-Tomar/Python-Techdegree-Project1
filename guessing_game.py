import random

name = input("What is your name? ")

print("Welcome to The Number Guessing Game! ")

start = input(f"Do you want to start the game {name}? (Y/N) ")

while start.title() == "Yes" or start.upper() == "Y":
  NUMBER = random.randint(1, 10)
  
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
  attempt = 1
  
  while guess != NUMBER:
    attempt += 1

    if guess > 10:
      print("Number must be in the range of 1 and 10.")
      guess = guess_number()
    
    elif guess > NUMBER:
      print("No, It's not that high. It's lower.")
      guess = guess_number()

    elif guess < NUMBER:
      print("No, it's not that low. It's higher.")
      guess = guess_number()

  print(f"You got it! You guessed it right {name}. The number is {NUMBER}")
  print(f"Attempts you took: {attempt}")
  print("GAME OVER!")

  start = input("Do you want to play again? (Y/N) ")
  continue

print(f"Thank you for showing interest in the game {name}!")
