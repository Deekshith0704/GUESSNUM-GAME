# import random
# num = random.randint(0,100)

# def gues():
#     global guess
#     guess = int(input("Guess a number between 0 and 100: "))
#     return guess

# while True:
#     guess = gues()
#     if (guess < num):
#       print("You're guessing too low!")
#     elif (guess > num):
#       print("You're guessing too high")
#     else:
#       print("You guessed it!")
#       break

import random
num = random.randint(0,100)
attempts = 0

difflevel = input("Enter the difficulty level (Easy,Medium,Hard) = ")

if(difflevel == "Hard"):
    attempts = 4
    print(f"You have {attempts} attempts left")

elif(difflevel == "Medium"):
    attempts = 6
    print(f"You have {attempts} attempts left")

elif(difflevel == "Easy"):
    attempts = 8
    print(f"You have {attempts} attempts left")

if(attempts == 1):
      print("Final try")

input("Press enter to start the game:")

while attempts>0:
    guess = input("Press 'Q' to quit || Guess a number between 0 and 100: ")
    attempts -= 1

    if(guess == 'Q'):
       print("GAME HAS BEEN QUIT")
       break
     
    else:
       guess = int(guess)
     
    if(guess < num):
          print("You are guessing too low")
    elif(guess > num):
          print("You are guessing too high")
    else:
          print("You guessed it right! Congratulations")
          break

    if attempts > 0:
        print(f"You have {attempts} attempts left.")
    else:
        print(f"------------GAME OVER------------! The number was {num}. \n      Try again you Dumb loser...")

