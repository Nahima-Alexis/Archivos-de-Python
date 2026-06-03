
import os
os.system("cls")
import random

print("--------------------------------------------")
print("-------------[GUESS THE NUMBER]-------------")
print("--------------------------------------------")

secret = random.randint(1,10)
while True:
    print(" ")
    guess = int(input("Enter a number\nHere ---> "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Oops, try again!")
    