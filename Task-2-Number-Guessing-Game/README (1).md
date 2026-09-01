# SYNENT Technology -- Task 2: Number Guessing Game

## Project Overview

This project is a beginner-friendly command-line Number Guessing Game
developed in Python as part of the SYNENT Technology Internship.

The program randomly selects a secret number between 1 and 100. The
player repeatedly enters guesses until the correct number is found.

## Objective

The objective of this task is to practice Python concepts including: -
Random number generation - User input - `while` loops - Conditional
statements - Comparison operators - Basic exception handling

## Features

-   Generates a random number between 1 and 100
-   Allows repeated guesses
-   Gives a "too high" hint
-   Gives a "too low" hint
-   Displays a success message when the number is guessed
-   Handles non-numeric input

## Technologies Used

-   Python 3
-   `random` module
-   Command Line Interface (CLI)

## Methodology

1.  The `random` module generates a secret number between 1 and 100.
2.  The program asks the player to enter a guess.
3.  A `while` loop continues the game until the secret number is
    guessed.
4.  If the guess matches the secret number, a congratulations message is
    displayed.
5.  If the guess is greater than the secret number, the program tells
    the player to guess smaller.
6.  If the guess is less than the secret number, the program tells the
    player to guess larger.
7.  Invalid non-numeric input is handled with a simple error message.

## How to Run

1.  Make sure Python 3 is installed.
2.  Open the project folder in VS Code or a terminal.
3.  Run:

``` bash
python number_guessing_game.py
```

4.  Enter whole-number guesses between 1 and 100.

## Example Output

``` text
===== NUMBER GUESSING GAME =====
Guess a number between 1 and 100.
Enter your guess: 50
Too high! Try a smaller number.
Enter your guess: 25
Too low! Try a larger number.
Enter your guess: 37
Congratulations! You guessed the correct number.
Game over. Thanks for playing!
```

## Screenshots

Add gameplay screenshots to the `screenshots` folder showing: - A "too
high" response - A "too low" response - A successful guess

## Project Structure

``` text
Task-2-Number-Guessing-Game/
│
├── number_guessing_game.py
├── screenshots/
│   ├── too_high.png
│   ├── too_low.png
│   └── success.png
├── report/
│   └── Number_Guessing_Game_Report.pdf
└── README.md
```

## Result

The game successfully generates a random number and guides the player
with higher/lower hints until the correct number is guessed.

## Conclusion

This project provides practical experience with random number
generation, loops, conditional logic, user input, and basic error
handling in Python.
