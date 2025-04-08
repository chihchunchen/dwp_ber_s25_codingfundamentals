# # Exercises on Functions and Imports

# ## HOMEWORK 1: Google time
# By using Google, find a function that gives you current date and time and print the current date and time
print("\nHOMEWORK 1")
# Import the 'datetime' module to work with date and time
import datetime

# Get the current date and time
now = datetime.datetime.now()
print(f"Current date and time : {now.strftime('%Y-%m-%d %H:%M:%S')}")


# ## HOMEWORK 2
# Do you still remember loops?
# 1. Write a function that counts number of letters in a string you input.
# 2. The function will have 1 parameter, the string that's letters you want to count.
# 3. Try both variants - print the result (number of letters in the inputed string) and also store the result in the memory using return. Try to recall what is the difference between using print and return
print("\nHOMEWORK 2")
def count_num_letters(string_input: str):
    return len(string_input)
def count_num_letters_loop(string_input: str):
    num_letters = 0
    for letter in string_input:
        num_letters+=1
    return num_letters

example_string = "A string with a number of letters"
n_letters = 0 
for letter in example_string:
    n_letters += 1
print(f"# letters just loop: {n_letters}")

n_letters_function1 = count_num_letters(example_string)
print(f"# letters function with len: {n_letters_function1}")

n_letters_function2 = count_num_letters(example_string)
print(f"# letters function with loop: {n_letters_function2}")


# ## HOMEWORK 3: Using results of function in another function
# 1. Create a simple function with two parameters that returns their sum.
# 2. Call the function and save the result into a variable (name of the variable is up to you).
# 3. Create another function with one parameter that decides if the parameter can be divided by 3 and prints appropriate messages
# 4. Call the second function and use the variable that you created in the b) part as argument.
print("\nHOMEWORK 3")
def sum_numbers(num1, num2):
    return num1 + num2
first_number = 3
second_number = 6
summed_numbers = sum_numbers(first_number, second_number)
print(f"The sum of {first_number} and {second_number} is {summed_numbers}")
def is_divisible_by_3(num):
    return num % 3 == 0
print(f"{summed_numbers} is divisible by 3: {is_divisible_by_3(summed_numbers)}")



# ## (Bonus) HOMEWORK 4: Rock, Paper, Scissors
# Here's what you need to do:
# 1. Complete the game logic inside the play_game(user_choice) function. The function should determine the outcome of the game based on the user's choice (0 for rock, 1 for paper, and 2 for scissors) and the computer's randomly generated choice.
# 2. The possible outcomes are as follows:
#    - If the user's choice is the same as the computer's choice, it's a "Tie."
#    - If the user wins, return "You win."
#    - If the computer wins, return "You lose."
# 3. Test the game by calling the function with different user choices and print the results.

# Reminder:
# - Rock beats Scissors
# - Scissors beats Paper
# - Paper beats Rock

print("\nHOMEWORK 4")
ROCK = 0
PAPER = 1
SCISSORS = 2
choice_map = {0: "Rock", 1: "Paper", 2: "Scissors"}
import random
def play_game(user_choice: int):
    computer_choice = random.randint(0, 2)
    outcome = "Invalid user choice"
    if user_choice == computer_choice:
        outcome = "Tie."
    elif user_choice == ROCK and computer_choice == PAPER:
        outcome = "You lose."
    elif user_choice == ROCK and computer_choice == SCISSORS:
        outcome = "You win."
    elif user_choice == PAPER and computer_choice == ROCK:
        outcome = "You win."
    elif user_choice == PAPER and computer_choice == SCISSORS:
        outcome = "You lose."
    elif user_choice == SCISSORS and computer_choice == ROCK:
        outcome = "You lose."
    elif user_choice == SCISSORS and computer_choice == PAPER:
        outcome = "You win."
    print(f"User choice: {choice_map[user_choice]}, Computer choice: {choice_map[computer_choice]}: {outcome}")
    return outcome

play_game(SCISSORS)
play_game(PAPER)
play_game(ROCK)

