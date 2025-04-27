import datetime
import random
import calc_utils
import pprint
import csv

# Create a simple number guessing game using if, elif, and else.
def numberGuesser():
    """
    A simple number guessing. 
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
            elif user_option.upper() =='R':
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
    for n in range(2,51,2):
        even_nums.append(n)
    print(f"Even numbers up to 50 are: {even_nums}")

    
# Create a phone book dictionary where the user can add and retrieve contacts.
def phonebook():
    phonebook_list = []
    def add_phonebook():

        try:
            name = input("Enter contact name: ").strip().title()
            phone = input(f"Enter '{name}' phonenumber: ").strip()
            if isinstance(name, str) and isinstance(phone, str):
                phonebook_list.append({"name": name, "phone": phone})
            else:
                raise ValueError
        except ValueError as e:
            return(f"****Please inform a valid value! You informed : '{name}' , phone: '{phone}'****\n")
        print ("Contact added!")

    def find_contacts():
        contacts_found=[]
        try:
            name = input("Enter the name to look up: ").strip().title()
            if isinstance(name, str):
                for item in phonebook_list:
                    contact = item.get("name")
                    if contact == name: 
                       contacts_found.append(item)
                if contacts_found:
                    return contacts_found
                else:
                    return "Not found!"
            else:
                raise ValueError
        except ValueError as e:
            return f"****Please inform a valid value, you informed: '{name}'****\n."
        
    def display_contacts():
        for item in phonebook_list:
            print(item)

    while True:
        option = input("*****Please choose an option:\n(A)dd a new contact;\n(F)ind a contact;\n(D)isplay contacts;\n(Q)uit.\n*****\n: ")
        if option.upper().strip() == 'A':
            add_phonebook()
        elif option.upper().strip() == 'F':
            print(find_contacts())
        elif option.upper().strip() == 'D':
            display_contacts()
        elif option.upper().strip() == 'Q':
            print("Thanks!")
            break
        else:
            print(f"****Please inform a valid option, you've chosen: '{option}'****\n")


#Ask the user for 5 numbers and print only the unique ones using a set.
def remove_duplicates(lst_items):
    unique_num = set()
    for item in lst_items:
        unique_num.add(item)
    return unique_num

# testing
# i = 0
# lst_num = []
# while i<5:
#     number = int(input("Inform a valid integer number..."))
#     lst_num.append(number)
#     i+=1
# print(remove_duplicates(lst_num))


# Create a text file, write a list of favorite movies to it, and read it back.
def write_to_text(movies, filename="dummy.txt"):
    with open(filename, "w", newline="\n") as file:
        file.write("Movie"+'\n')
        for movie in movies:
            file.write(movie+'\n')

def read_from_txt(filename):
    with open(filename, "r") as file:
        return file.read()

# list_movies=["Pride and Prejudice", "Doctor Strange", "Resident Evil"]
# write_to_text(list_movies, "fave_movies.txt")
# print(read_from_txt("fave_movies.txt"))




    
