# Lesson 2 
# Introduction to Python: Variables, Data Types & Booleans  
                                                           


## 1. Variables and Basic Data Types
#a. Assign the number 10 to a variable named `my_number`.
my_number = 10

#b. Assign the string "Hello, Python!" to a variable named `my_string`.
my_string = "Hello, Python!"

#c. Assign the float 3.14 to a variable named `my_float`.
my_float = 3.14

#Print each variable: `my_number`, `my_string`, and `my_float`.
print(f"my_number: {my_number}")
print(f"my_string: {my_string}")
print(f"my_float: {my_float}")

## 2. Working with Different Data Types
#**a. String concatenation**
#- Create two string variables: `first_name` and `last_name`.
first_name = 'Chih-Chun'
last_name = 'Chen'
#- Concatenate them with a space in between to form a full name and assign this to a variable named `full_name`.
full_name = first_name + ' ' + last_name
#- Print the full_name.
print(f"full_name: {full_name}")

#**b. Arithmetic Operations**
#- Create two integer variables: `a = 5` and `b = 3`.
a = 5
b = 3

#- Perform addition, subtraction, multiplication, and division on these variables, e.g., a+b, a-b, a*b, a/b, and save each result to `add_result`, `sub_result`, `mult_result`, `div_result`
add_result = a + b
sub_result = a - b
mult_result = a * b
div_result = a/b

#- Print the results of each operation.
print(f"add_result: {add_result}")
print(f"sub_result: {sub_result}")
print(f"mult_result: {mult_result}")
print(f"div_result: {div_result}")

## 3. Booleans and Comparisons

#**a. Creating booleans**
#- Assign the result of 5 > 3 to a variable named `is_greater`.
is_greater = 5 > 3
#- Assign the result of 5 == 3 to a variable named `is_equal`.
is_equal = 5==3
#- Assign the result of 5 < 3 to a variable named `is_smaller`.
is_smaller = 5 < 3
#- Print the values of `is_greater`, `is_equal`, and `is_smaller`.
print(f"is_greater: {is_greater}")
print(f"is_equal: {is_equal}")
print(f"is_smaller: {is_smaller}")

#**b. Boolean Operations**

#Create two boolean variables: `bool1 = True` and `bool2 = False`.
bool1 = True
bool2 = False
#Perform logical AND, OR, and NOT operations on these variables and print the results.
and_result = bool1 & bool2
or_result = bool1 | bool2
not_bool1_result = not bool1
not_bool2_result = not bool2
not_and_result = not and_result
not_or_result = not or_result

print(f"and_result: {and_result}")
print(f"or_result: {or_result}")
print(f"not_bool1_result: {not_bool1_result}")
print(f"not_bool2_result: {not_bool2_result}")
print(f"not_and_result: {not_and_result}")
print(f"not_and_result: {not_or_result}")

#**c. Comparison between data types**

#Given three variables:
#```
#pi = 3.14
#pi_pi = '3.14'
#pi_pi_pi = "3.14"
#```
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"

#1. Are `pi` and `pi_pi` equal? If not, why?
print(f"Are `pi` and `pi_pi` equal?: {pi==pi_pi}")
#2. Are `pi_pi` and `pi_pi_pi` equal? If not, why?
print(f"Are `pi_pi` and `pi_pi_pi` equal?: {pi_pi==pi_pi_pi}")


## 4. Type checking and conversion.
#**a. Type checking**

#For each variable `pi`, `pi_pi`, `pi_pi_pi`, use the type() function to print its data type.
print(f"type(pi): {type(pi)}")
print(f"type(pi_pi): {type(pi_pi)}")
print(f"type(pi_pi_pi): {type(pi_pi_pi)}")

#**b. Type conversion**

#- Create a string variable `my_str = "123"`.
my_str = "123"
#- Convert it to an integer and store it in a variable named `my_int`.
my_int = int(my_str)
#- Convert `my_int` to a float and store it in a variable named `my_float_converted`.
my_float_converted = float(my_int)
#- Print all three variables.
print(f"my_str: {my_str}")
print(f"my_int: {my_int}")
print(f"my_float_converted: {my_float_converted}")

## 5. Challenge

#- Define a variable `celsius` and assign it a temperature value in Celsius.
celsius = 30
#- Use the formula (celsius * 9/5) + 32 to convert the temperature to Fahrenheit.
#- Store the result in a variable named `fahrenheit`.
farenheit = (celsius * 9/5) + 32
#- Print the original temperature in Celsius and the converted temperature in Fahrenheit.
print(f"{celsius} celsius = {farenheit} farenheit")

