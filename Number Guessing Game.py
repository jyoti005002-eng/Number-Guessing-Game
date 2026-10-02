"""Requirements
It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

When the game starts, it should display a welcome message along with the rules of the game.

The computer should randomly select a number between 1 and 100.

User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.

The user should be able to enter their guess.

If the user's guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.

If the user's guess is incorrect, the game should display a message indicating whether the number is greater or less than the user's guess.

The game should end when the user guesses the correct number or runs out of chances."""

print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100")
print("You have 5 chances to guess the correct number .\n")

print("Please select the difficulty level : ")
print(" Click 1 for easy (You will get 10 chances)")
print(" Click 2 for medium (You will get 5 chances)")
print(" Click 3 for difficult (You will get 3 chances)\n")

while True : 
    Level = int(input("Enter Your Choice : "))

    if(Level == 1 ):
        attempts = 10 
        print("Great ! You have selected the Easy difficulty level " )
        print(" Let's start the game !")
        break
    

    elif(Level == 2 ):
        attempts = 5 
        print("Great ! You have selected the Medium difficulty level " )
        print(" Let's start the game !")
        break

    elif(Level == 3 ):
        attempts = 3
        print("Great ! You have selected the Difficult difficulty level" )
        print(" Let's start the game !")
        break

    else:
        print("Invalid Input")

        exit()


import random 
number = random.randint(1,100)

for attempt in range(1 , attempts + 1 ):
    guess = int(input ("Attempt " + str(attempt) + ": Enter your number : "))

    if (number> guess):
        print("Incorrect! The number is greater than " , guess)

    elif (number<guess):
        print("Incorrect! The number is less than " , guess)

    else:
        print("Congratulations! You guessed the correct number in", str(attempt)," attempts.")
        break 

print("GAME OVER !!")