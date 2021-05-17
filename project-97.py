print("*Number Guessing Game*")
print("Guess a number between 1-9")
from random import randrange
chances = 0
number = randrange(1,9)

while chances<5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("congratulation,YOU WON!!")
        break

    elif guess <= number:
        print("your guess is too low,try a higher number than",guess)
        chances+=1

    else:
        print("your guess is too high,try a lower number than",guess)
        chances+=1
        

if chances == 5:
    print("\nyour all guesses are wrong,thank you for playing")      