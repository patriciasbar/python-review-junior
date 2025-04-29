"""
Types
Basic: [expression for item in iterable]
If/Else: [expression_if_true if condition else expression_if_false for item in iterable]
Nested: [expression for item1 in iterable1 for item2 in iterable2]
If/Else Nested: [expression_if_true if condition else expression_if_false for item1 in iterable1 for item2 in iterable2]
"""

# Create a list of the squares of numbers from 0 to 9.
squared_nums = [x**2 for x in range(0,10)]
#print(squared_nums)

#Make a list containing all letters in the word "Gratitude".
letters_list = [word for word in "Gratitude"]
#print(letters_list)

#For numbers 0 to 9, create a list where each number is replaced by "big" if it is greater than 5, otherwise "small".
nums_list = ["big" if x > 5 else "small" for x in range(0,10)]
#print(nums_list)

#Given a list of temperatures in Celsius, make a new list with "hot" if the temperature is over 30, otherwise "cool".
temperature_celsius = ["hot" if i > 30 else "cool" for i in range(0,100, 15)]
#print(temperature_celsius)


#Create a list of all possible sums of two numbers, where the first number is from 0 to 2 and the second number is from 0 to 3.
sum_of_combinations = [x+y for x in range(3) for y in range(4)]
#print(sum_of_combinations)

#Make a list of all pairs (x, y) where x is from "abc" and y is from "12".
pair_combinations = [(x,y) for x in ("abc") for y in ("12")]
#print(pair_combinations)

#Create a list of (x, y) if x is not equal to y; otherwise, put "match" for x from 0 to 2 and y from 0 to 2.
list_matches = [(x,y) if x!=y else (x, "match") for x in range(3) for y in range(3)]
#print(list_matches)

#Make a list where for each combination of day and temperature # (days = ["Mon", "Tue"], temps = [20, 35]), 
# you put (day, "hot") if temp > 30, else (day, "cool").
days = ["Mon", "Tue"]
temps = [20,35]
list_days_temps = [(day, "hot") if temp > 30 else (day, "cool") for day, temp in zip(days, temps)] 
#print(list_days_temps)


