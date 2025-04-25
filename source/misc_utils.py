import datetime
import random
import calc_utils

# Create a simple number guessing game using if, elif, and else.
def numberGuesser():
    """
    A simple number guessing. Up to 5 tries.
    """
    secret_number = random.randint(1,22)
    try:
        guess = int(input("What is the secret number from 1 to 22? Enter a guess (integer)..."))
        if guess < 1 or guess > 22:
            return f"Guess should be within the range 1-22. You entered {guess}"
        else:
            if guess == secret_number:
                return f"Yeah! You got it right! secret number is {secret_number} and you guessed {guess}!"
            else:
                return f"Nope! Secret number is {secret_number} and your guess was {guess} Good luck the next time!"
    except Exception as e:
        return f"An error occurred! {e}"

# Write a program that checks if a number is between 10 and 20 and is even.
def checkNumber(n):
    """
    Check a given valid integer number `n` and returns if it is:
    between 10 and 20;
    an even number;
    """
    if not isinstance(n, int):
        return f"Please inform a valid integer number. You informed {n}."
    else:
        is_between_range = f"is" if n > 9 and n < 21 else "is not"
        return f"{n} is {calc_utils.isEvenOrOdd(n)} and {is_between_range} between 10 and 20"


# Print the multiplication table for a number given by the user (up to 10).
def multiply_by_10(n):
    if isinstance(n, int):
        for i in range(11):
            template = f"|{n:2} x {i:2} = {calc_utils.multiplication(n,i):4}|"
            print(template)
    else:
        return f"Please inform a valid integer number, you informed: '{n}'"


#Create a list of 5 items, let the user add one item, and then remove one. Print the final list.
def update_list():
    list_items = ["Peace","Gratitude","Joy","Happiness","Love"]
    while True:
        print(f"Current items: {list_items}")
        user_option = input("Do you want to Add(A) or Remove(R) an item from this list? type 'Q' to quit..." )
        if isinstance(user_option, str):
            if user_option.upper() == 'Q':
                break;
            elif user_option.upper() == 'A':
                uvalue = input("Enter new value: ")
                if uvalue:
                    list_items.append(uvalue)
                    print(f"New value {uvalue} added!")
                else:
                    print(f"Please inform a value!")
            elif user_option =='R':
                uvalue = input("Enter value to be removed: ")
                if uvalue in list_items:
                    list_items.remove(uvalue)
                    print(f"Value {uvalue} removed!")
                else:
                    print(f"Value {uvalue} does not exist within the list!")
            else:
                print(f"Enter a valid value!")
        else:
            print(f"Enter a valid value!")
    return list_items


# Print all even numbers between 1 and 50 using range().
def print_even_numbers():
    """
    Prints even numbers up to 50.
    """ 
    even_nums=[]   
    for n in range(0,51,2):
        even_nums.append(n)
    print(f"Even numbers up to 50 are: {even_nums}")

    
print_even_numbers()