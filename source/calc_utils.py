import datetime
import math
#Write a script that calculates the area of a rectangle. 
##Use comments to explain each step.
def multiplication(n1, n2):
    """
    Returns the product of two numbers (n1, n2)
    """
    return n1*n2


def calcRectangle(length, width):
    """
    Calculates the area of a rectangle.
    """
    # checks if valid input
    if isinstance(length, (int,float)) and isinstance(width, (int,float)):
        return length * width
    else:
        return f"Enter a valid input or inputs!"

# Ask the user for two numbers and print the sum, difference, product, and quotient.
def simpleMathOperations():
    """
    Calculates the sum, difference, product and quotient of given 2 numbers.
    """
    results = {}
    try:
        n1=int(input("Enter n1 (integer): "))
        n2=int(input("Enter n2 (integer): "))
        # addition
        results["Sum"]=n1+n2
        # subtraction
        results["Difference"]=n1-n2
        # multiplication
        results["Multiplication"]=multiplication(n1,n2)
        # division
        if n2==0:
            raise ZeroDivisionError
        else:
            results["Division"]=n1/n2
        return f"Results for {n1} and {n2} numbers: {results}"
    except ValueError as e:
        return f"Please enter a valid integer. {e}"
    except ZeroDivisionError as e1:
        return f"Cannot divide by zero! {n2}"

# Write a program that asks the user for their birth year and calculates their age.
def calcAge():
    """
    Calculates users age based on their birth year.
    Returns an error if not a valid year (1900 to now(year))
    """
    today_year = int(datetime.datetime.now().strftime("%Y"))
    try:
        birth_year = int(input("What is your birth year? "))
        if birth_year > today_year or birth_year < 1900:
            raise ValueError("Enter a valid year.")
        else:
            return today_year - birth_year
    except Exception as e:
        return f"Invalid input. {e}"

def isEvenOrOdd(n):
    """
    Returns if a given number is even or odd.
    """
    if n%2==0:
        return f"Even"
    else:
        return f"Odd"


#Write a function that takes two numbers and returns their average.
def calcAverage(n1,n2):
    """
    Returns average between two numbers.
    """
    if isinstance(n1, (int, float)) and isinstance(n2, (int,float)):
        return (n1+n2)/2   
    else:
        return None


# Write a program that stores coordinates as tuples and prints their distances from the origin.
def distanceCoordinates(o1, o2, p1, p2):
    if type(o1) == type(o2) == type(p1) == type(p2):
        origin=(o1, o2)
        coordinates=(p1,p2)
        return (coordinates[0] - origin[0], coordinates[1] - origin[1])
    else:
        return None
    

# Use the math module to calculate the square root and power of user-provided numbers.
def calcsqrt(n):
    return math.sqrt(n)

def calcpow(n):
    return math.pow(n,2)
