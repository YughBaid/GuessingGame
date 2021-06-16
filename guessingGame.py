import random

number = random.randrange(1,20)
guess = int(input("guess a number between 1 to 20: "))
chances = 0

while chances < 5:
    if guess == number:
        print("you guessed the number correctly!")
        break
    elif guess > number:
        print("you need to guess lower")
        guess = int(input("guess a number between 1 to 20: "))
    else:
        print("you need to guess higher") 
        guess = int(input("guess a number between 1 to 20: "))

    chances=chances+1

if not chances < 5:
    print("YOU LOOSE!!, the number is: ",number)

