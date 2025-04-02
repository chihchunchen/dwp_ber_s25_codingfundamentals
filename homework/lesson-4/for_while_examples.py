list_of_numbers = [9, 6, 2, 3, 4]
sum_of_numbers = 0
print("for-loop")
for i in list_of_numbers:
    sum_of_numbers = sum_of_numbers + i
print("sum")
print(sum_of_numbers)

sum_of_numbers = 0
print("while-loop")
i = 0
while i < len(list_of_numbers):
    sum_of_numbers = sum_of_numbers +list_of_numbers[i]
    i = i + 1
print("sum")
print(sum_of_numbers)

a_dictionary = {'key1': 'giraffe', 'key2': 'elephant'} 
print(a_dictionary['key1'])
a_dictionary['anyothername'] = 'human'
print(a_dictionary['anyothername'])