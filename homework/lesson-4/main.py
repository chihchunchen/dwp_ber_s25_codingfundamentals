# Exercises on Data Structures (Lists, Sets, Tuples)             

## Exercise 0
"""Given the following scores, what is the length of the list?"""
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
scores_length = len(scores)
print("\nE0")
print(f"scores_length: {scores_length}")

## Exercise 1:
"""Given the same list of scores, write a program that counts the number of 3s in the list"""
print("\nE1")
## Implemented with loop
num_threes = 0
for num in scores:
    if num==3:
        num_threes += 1
print(f"#3s (loop): {num_threes}")

## Implemented with list comprehension
scores3 = [x for x in scores if x==3]
scores3_length = len(scores3)
print(f"#3s (list comprehension): {scores_length}")

## Exercise 2:
"""Given the same list of scores, find the maximum in the list"""
print("\nE2")
max_score = max(scores)
print(f"Max scores: {max_score}")


## Exercise 3:
"""Given the following two lists, write a program that prints the common elements"""

print("\nE3")
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
common_elements = set(list_1).intersection(set(list_2))
print(f"Common elements: {common_elements}")

## Exercise 4:
"""
Given the following list of numbers, write a program
1. that goes through each number in the list
2. appends it to a new list called `positive_numbers` if the number is positive"
"""
print("\nE4")
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
for num in all_numbers:
    if num > 0:
        positive_numbers.append(num)
print(f"Positive numbers: {positive_numbers}")    

## Exercise 5:
"""Print the items of the given list in reverse"""
print("\nE5")
reverse_this_list = [10, 20, 30, 40, 50]
reversed_list = reverse_this_list[::-1]
print(f"reversed_list: {reversed_list}")


## Exercise 6
"""Convert the scores list (from Exercise 0) into a set and print its elements"""
print("\nE6")
scores_set = set(scores)
print(f"scores_set: {scores_set}")
for score in scores_set:
    print(score)

## Exercise 7
"""
Create a List of Tuples with 5 country names and their capitals, and print the list

Each tuple should contain one country and its capital
"""
print("\nE7")
country_tuples = [("United Kingdom", "London"), ("France", "Paris"), ("Germany", "Berlin"), ("Poland", "Warsaw"), ("Ireland", "Dublin")]
print(f"country_tuples: {country_tuples}")