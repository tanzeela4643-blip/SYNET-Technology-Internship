# SYNET Technology -- Task 1: Simple Calculator

## Project Overview

This project is a beginner-friendly command-line Simple Calculator
developed in Python as part of the SYNET Technology Internship.

The program takes two numeric values and an arithmetic operator from the
user and calculates the result.

## Objective

The objective of this task is to demonstrate basic Python programming
concepts such as: - User input - Numeric data types - Conditional
statements - Arithmetic operators - Basic error handling - Command-line
output

## Features

-   Addition (`+`)
-   Subtraction (`-`)
-   Multiplication (`*`)
-   Division (`/`)
-   Division-by-zero error handling
-   Invalid operator handling

## Technologies Used

-   Python 3
-   Command Line Interface (CLI)

## Methodology

1.  The program displays a calculator heading.
2.  The user enters two numbers.
3.  The user enters an arithmetic operator.
4.  Conditional statements identify the selected operation.
5.  The calculation is performed and the result is displayed.
6.  If the user attempts to divide by zero, an error message is
    displayed.
7.  If an unsupported operator is entered, the program displays an
    invalid-operator message.

## How to Run

1.  Make sure Python 3 is installed.
2.  Open the project folder in VS Code or a terminal.
3.  Run:

``` bash
python simple_calculator.py
```

4.  Enter the requested values and operator.

## Example Output

``` text
===== SIMPLE CALCULATOR =====
Enter value of A: 20
Enter value of B: 10
Enter operator (+, -, *, /): +
Result: 30.0
```

## Screenshots

Add the following screenshots to the `screenshots` folder:

-   `addition.png`
-   `subtraction.png`
-   `multiplication.png`
-   `division.png`
-   `division_by_zero.png`

Then they can be displayed here:

``` text
screenshots/
├── addition.png
├── subtraction.png
├── multiplication.png
├── division.png
└── division_by_zero.png
```

## Project Structure

``` text
SYNET-Task-1-Simple-Calculator/
│
├── simple_calculator.py
├── screenshots/
│   ├── addition.png
│   ├── subtraction.png
│   ├── multiplication.png
│   ├── division.png
│   └── division_by_zero.png
├── report/
│   └── Simple_Calculator_Report.pdf
└── README.md
```

## Result

The calculator successfully performs the four basic arithmetic
operations and handles invalid input cases such as division by zero and
unsupported operators.

## Conclusion

This task provides practical experience with Python fundamentals,
especially input handling, conditional logic, arithmetic operations, and
basic error handling.
