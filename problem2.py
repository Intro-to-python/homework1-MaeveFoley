#homework1
#Due 10/10/18

# Problem 2
#Write a Python program to guess a number between 1 to 9.
# User is prompted to enter a guess. If the user guesses wrong then
#the prompt appears again until the guess is correct, on successful guess,
#user will get a "Well guessed!" message, and the program will exit.
#(Hint use a while loop)
#Don't forget to import random

import random
targetNum = random.randint(1,9)
guessNum = input("Enter a number")
while guessNum = targetNum:
  print("Well guessed!")
else:
  print(input("Try again!"))
