import datetime

# Print a greeting message that includes your name and today’s date.
def greeting():
    """
    Asks users for their name.
    Returns a greeting message and today's date.
    """
    name = input("What's your name? ")
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    return (f"Hello, {name}! Today is {today}!")
    
# Create variables for a person's name, age, and height. Print them with labels.
def personDetails():
    """
    Asks user for their Name, Age and Height.
    Returns these details with labels.
    """
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        height = float(input("Please enter your height (cm): "))
        return f"Name: {name}\nAge {age}\nHeight {height}  " 
    except Exception as e:
        return f"Please enter a valid input. {e}"

#Ask the user for a sentence and print the number of characters, words, and the sentence reversed.
def checkStringLen(s):
    """
    Returns the length of a given sentence. (including white spaces)
    """
    return len(s);

def countWords(s):
    """
    Return the number of words within a given sentence. (Only alphabetic words)
    """
    count = 0
    for word in s.split():
        if word.isalpha():
            count += 1
    return count

def reverseSentence(s):
    """
    Returns a given sentence reversed.
    """
    return s[::-1]

def funnyString():
    """
    Asks user for a sentence.
    Returns its length, unique words and reversed sentence.
    """
    sentence = input("Hey there! enter a sentence...")
    string_len = checkStringLen(sentence)
    count_words = countWords(sentence)
    reversed_sentence = reverseSentence(sentence)
    return f"Your original sentence has {string_len} chars, a total of {count_words} words and it is now reversed: {reversed_sentence}!!!"


