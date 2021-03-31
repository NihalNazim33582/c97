import random

print("Lets play a Guessing Game")

nummm = random.randint(0,45)

chances = 0

print("Guess any number between 0 To 45")


while chances<5:
    guess = int(input("ENTER YOUR GUESS"))

    if guess == nummm:
        print("CORRECT!")
        break
    
    elif guess < nummm:
        print("Your guess was too low.")
        print("Try and guess a number higher than this.")

    else:
        print("Your guess was too high.")
        print("Try and guess a number lower than this.")
    
    chances+=1

if chances==5 and guess!= nummm:
    print("YOU LOSE")