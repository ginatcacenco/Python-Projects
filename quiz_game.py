"""
The idea behind the game is that we ask the user a series of questions and if he gives us the right answer, he will
receive 1 point for each correct answer. After the user has answered all questions, he will be able to find out what
his score is.
"""

print("Welcome to my computer quiz!")  # Greet the user with a welcome message
playing = input("Do you want to play? ")  # Ask the user if he wants to play the game
if playing.lower() != "yes":  # If the user's answer is: YES, YeS, YEs or Yes, the condition will still be true
    quit()  # If the user's answer is not yes, we will quit the game
print("Ok! Let's play!")
score = 0

answer = input("What does GUI stand for? ")
if answer.title() == "Graphical User Interface":  # Compare the user's answer with te correct answer
    print("Correct!")
    score += 1  # If the user's answer is correct, he will receive 1 point for his correct answer
else:
    print("Incorrect!")  # If the user's answer is wrong, he will receive a message to that effect

answer = input("What does SQL stand for? ")
if answer.title() == "Structured Query Language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CSS stand for? ")
if answer.title() == "Cascading Style Sheets":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does URL stand for? ")
if answer.title() == "Uniform Resource Locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.title() == "Application Programming Interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You answered {score} questions correctly!")  # Calculation of user score
