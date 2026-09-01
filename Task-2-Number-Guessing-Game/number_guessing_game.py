# SYNENT Technology - Data Science Internship
# Task 2: Number Guessing Game

import random

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100.")

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")

        elif guess > secret_number:
            print("Too high! Try a smaller number.")

        else:
            print("Too low! Try a larger number.")

    except ValueError:
        print("Please enter a valid whole number.")

print("Game over. Thanks for playing!")
