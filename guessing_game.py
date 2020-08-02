"""
Treehouse Python Techdegree
Project 1 - Number Guessing Game
Elijah Thomas
/2020
"""

"""
Tried to make my code a bit fancy. I have a bit of knowledge beyond what's been taught to me thus
far in the techdegree, and I plan to use it to streamline the program as much as I can.
"""

#Also, fair warning, I use a ton of \n newlines to make the output look better.

import random

def start_game():
    guesses = 0 #Amount of user's guesses so far
    feedback = "What is your guess?" #This variable will be what's printed when asking the user for their guess. It changes based on the user's answer and how it relates to the answer (lesser/greater)
    plural = "guess" #This just determines whether "guess" or "guesses" is printed at the end of the game, just a grammatical fix.
    guessed = [] #List containing any numbers the player has already guessed.
    answer = random.choice(range(1, 11))
    print("\nWelcome to my number guessing game!\nI'm going to pick a number between 1 and 10. Can you guess what it is?\n")
    while True: #Main loop in which the entire game runs. Breaks when the user wins.
        while True: #Loop to obtain acceptable input (integer 1-10). Will only break if this is achieved.
            userInput = input(f"\n{feedback}\n\n")
            try:
                userInt = int(userInput)
                if userInt < 1:
                    print("\nThat's too low!")
                    raise ValueError
                elif userInt > 10:
                    print("\nThat's too high!")
                    raise ValueError
                break
            except ValueError:
                print("\nPlease enter a whole number between 1 and 10.")
        guesses += 1
        if guesses > 1:
            plural = "guesses"
        if userInt == answer:
            break #This will break the main loop, and the user will win the game.
        elif userInt < answer:
            feedback = "The answer's bigger!"
        else:
            feedback = "The answer's smaller!"
        if userInt in guessed:
            feedback += " You already guessed that!" #Adds a comment to the feedback variable if the user already guessed this number.
        else:
            guessed.append(userInt) #Adds the user's input into the list of guesses if it's not already there.
    if input(f"\nCongratulations! You guessed it! The answer was {answer}! You got it in {guesses} {plural}!\n\nPlay again? (y/n)\n\n") in ("y", "Y", "yes", "Yes"): #This is a long line, but it basically announces that you won and asks if you want to play again, all in the same stroke.
        start_game()
    else:
        exit()

start_game()

#I was going for the "exceeds expectations" requirements for this project, but chose to omit the high-score system. I thought it'd be a bit too tedious to implement it, so I'm good with just meeting the expectations.
