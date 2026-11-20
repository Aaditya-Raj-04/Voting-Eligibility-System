# Voting-Eligibility-System

## Project Overview

The Voting Eligibility System is a Python-based console application that checks whether a person is eligible to vote based on their age and Indian citizenship.

## Problem Statement

The program takes a person's name, age and citizenship as input. It checks whether the person is eligible to vote and displays the appropriate reason when the person is not eligible.

The program also allows multiple voters to be checked using a loop and handles invalid age input using exception handling.

## Eligibility Criteria

A person is eligible to vote when:

- Age is 18 or above
- The person is an Indian citizen

The valid age range is from 0 to 120.

## Technologies Used

- Python 3
- Console/Terminal
- Git and GitHub

## Python Concepts Used

- Variables
- Input and Output
- Conditional Statements
- Functions
- While Loops
- Exception Handling
- Boolean Conditions

## Features

1. Takes the voter's name.
2. Accepts and validates age.
3. Checks Indian citizenship.
4. Determines voting eligibility.
5. Displays the reason for ineligibility.
6. Calculates years left for people below 18.
7. Handles invalid age input.
8. Allows multiple voters to be checked.
9. Displays the final voter count.

## Test Cases

| Test Case         | Input       |   | Expected Result                   |
| ----------------- | ----------- | - | --------------------------------- |
| Normal Input      | Aman, 25, y |   | Aman is eligible to vote          |
| Boundary Input    | Neha, 18, y |   | Neha is eligible to vote          |
| Below Eligibility | Ravi, 17, y |   | Ravi is not eligible; 1 year left |
| Invalid Input     | Amit, abc   |   | Invalid input message             |
| Invalid Age       | Amit, -5    |   | Invalid age message               |
| Non-Citizen       | Riya, 30, n |   | Riya is not eligible              |

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python voting_eligibility.py
```

5. Enter the requested information.

## Conclusion

This project demonstrates the use of conditional statements, functions, loops and exception handling in Python to build a simple voting eligibility system.
