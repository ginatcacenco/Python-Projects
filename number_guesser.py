"""
The idea behind this project is to generate a random number, and we're going to track how many times it takes the user
to guess this number.
"""

import random

top_of_range = input("Type a number: ")  # Ask the user how large of a number he wants to generate

if top_of_range.isdigit():  # Make sure that the user typed a number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number larger than 0 next time.")
        quit()
else:
    print("Type a number next time.")  # Warning message if the user types something other than a number
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:  # Ask the user to make a guess for the number until he gets if correct
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():  # Make sure that the user typed a number
        user_guess = int(user_guess)
    else:
        print("Type a number next time.")  # Warning message if the user types something other than a number
        continue

    if user_guess == random_number:
        print("You got it!")
        break  # Break out of the loop as soon as the user types in the correct number
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses.")  # Print how many guesses the user got
