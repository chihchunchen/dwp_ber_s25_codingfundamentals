# Python Exercises

import random


## Exercise 1: Student Grouping
#Imagine you are a teacher who needs to group their students into pairs or small groups. 
# Given the following list of dictionaries, create random pairs or groups of students – each pair has to have the same project choice.


students = [
    {
        "name": "Jane",
        "choice": "Project B"
    },
    {
        "name": "Janet",
        "choice": "Project A"
    },
    {
        "name": "Jack",
        "choice": "Project A"
    },
    {
        "name": "Jimmy",
        "choice": "Project B"
    },
    {
        "name": "Jean",
        "choice": "Project A"
    },
    {
        "name": "Juan",
        "choice": "Project B"
    },
    {
        "name": "Juanita",
        "choice": "Project B"
    },
    {
        "name": "Janine",
        "choice": "Project A"
    },
    {
        "name": "Jill",
        "choice": "Project B"
    },
    {
        "name": "John",
        "choice": "Project B"
    }#,
    #{
    #    "name": "Jonny",
    #    "choice": "Project B"
    #},
]


#Example pairs:
#- Pair 1: [John, Jane] (they both have Project B)
#- Pair 2: [Janine, Janet] (they both have Project A)

#You can use the following helper function:
def pick_random_name(list_names):
    random_name = random.choice(list_names)
    return random_name


project_lists = {}
for student in students:
    k = student['choice']
    if k not in project_lists:
        project_lists[k] = [student['name']]
    else: 
        project_lists[k].append(student['name'])

pairs = []
for project in project_lists.keys():
    project_names = project_lists[project]
    while len(project_names) >= 2:
        
        student_1 = pick_random_name(project_names)
        student_2 = pick_random_name(project_names)
        if student_1!=student_2:
            pair = [student_1, student_2]
            project_names.remove(student_1)
            project_names.remove(student_2)   
             
            if len(project_names)==1:
                pair.append(project_names[0])
            pairs.append(pair)

print(f"Project pairs: {pairs}")

    

#**Bonus**: Make your code into a function which returns the list of pairs.

def get_pairs(project_dicts):
    project_lists = {}
    for student in project_dicts:
        k = student['choice']
        if k not in project_lists:
            project_lists[k] = [student['name']]
        else: 
            project_lists[k].append(student['name'])

    pairs = []
    for project in project_lists.keys():
        project_names = project_lists[project]
        
        while len(project_names) >= 2:
        
            student_1 = pick_random_name(project_names)
            student_2 = pick_random_name(project_names)
            if student_1!=student_2:
                pair = [student_1, student_2]
                project_names.remove(student_1)
                project_names.remove(student_2)   
             
                if len(project_names)==1:
                    pair.append(project_names[0])
                pairs.append(pair)
    return pairs

print(f"Project pairs with function: {get_pairs(students)}")


## Exercise 2: Meal cost calculator
### Preparation
#Run the following code a few times to understand what is happening. The 'inquire' function will ask 3 questions for each person. 
# You don't need to understand how the 'inquire' function works, you just need to use it. 
# You will be able to select one of two options for each question asked. 
# You will then need to do some calculations based on the result created by the 'inquire' function.


import inquirer
import random

def inquire(name):
  breakfast_base = random.randint(2, 6)
  lunch_base = random.randint(10, 21)
  dinner_base = random.randint(30, 51)
  questions = [
      inquirer.List(
          "breakfast",
          message=f"How much did {name} pay for breakfast? 🥐 ☕",
          choices=[f"${breakfast_base}", f"${breakfast_base + 2}"],
      ),
      inquirer.List(
          "lunch",
          message=f"How much did {name} pay for lunch? 🍔",
          choices=[f"${lunch_base}", f"${lunch_base + 7}"],
      ),
        inquirer.List(
          "dinner",
          message=f"How much did {name} pay for dinner? 🍽️",
          choices=[f"${dinner_base}", f"${dinner_base + 15}"],
      ),
  ]
  
  transactions = inquirer.prompt(questions)
  return {name: transactions}

people = ["John", "Jane", "Janet"]
result = [inquire(person) for person in people]
print("Result: ")
print(result)


#Write a function which calculates the sum of the 3 meals for each friend (use the 'result' variable as input to your function).
def sum_transactions(trans_dict):
    num_transactions = sum([float(cost.strip('$')) for meal, cost in trans_dict.items()])
    return num_transactions

def sum_meals(meal_dicts):
    return [{name: f"${sum_transactions(transactions):.0f}"} for d in meal_dicts for name, transactions in d.items()]

print(f"Totals: {sum_meals(result)}")

#Example output:
#- Jane sum: $74

#The `convert_dollars` function will help you convert the strings given in our result list into numbers that you can use to perform calculations. From $X (type str) to X (type int)


def convert_dollars(value):
    number_value = int(value.replace("$", ""))
    return number_value

def sum_transactions(trans_dict):
    num_transactions = sum([convert_dollars(cost) for meal, cost in trans_dict.items()])
    return num_transactions

def sum_meals(meal_dicts):
    return [{name: f"${sum_transactions(transactions):.0f}"} for d in meal_dicts for name, transactions in d.items()]

print(f"Totals with convert_dollars function: {sum_meals(result)}")


#**Bonus**: - Replace the value of the name variable with your own name.

## Exercise 4: Meal cost game
#Run this code a few times and try to understand how the game works to then be 
#able to try and win the game. Slightly change the low and high limit range to make the game easier to win.

def play_game():
    name = "ReDi"
    lower_limit = 42 
    higher_limit = 55 
    meals = inquire(name)[name] 
    total = 0

    for meal_value in meals.values(): 
        total += convert_dollars(meal_value) 
    if (lower_limit > total or higher_limit < total): 
        print("You lost.. try again!") 
    else: 
        print("Congrats! You won 👏")

# Uncomment the lines below to test your answer 👇👇👇
# play_game()


## Exercise 4: Credit Card Masking
#Complete the `mask_credit_card_number` function that takes in a 16-digit credit card number and masks all but the last 4 digits.

def is_int_string(a_string):
    try:
        int(a_string)
        return True
    except:
        return False

sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    if isinstance(credit_card_number, str) and len(credit_card_number)==16 and is_int_string(credit_card_number):
        masked_credit_card_number = f"XXXXXXXXXXXX{credit_card_number[-4:]}"
        
        return masked_credit_card_number

# Uncomment the lines below to test your answer 👇👇👇
print('Expected result: ', expected_credit_card_result)
result = mask_credit_card_number(sample_credit_card_number)
print('Your result:', result)

