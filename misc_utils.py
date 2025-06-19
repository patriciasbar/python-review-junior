from functools import reduce
from abc import ABC, abstractmethod

def bill_calculator(*args):
    return sum(args)

             
def person_details(**kwargs):
    details = ""
    for k, v in kwargs.items():
        details = details + f"{k}={v}" + ","
    return details[:-1]


def custom_order(product, *args, **kwargs):
    order_summary = {}
    order_summary["Product"] = product
    order_summary["Cities"]= args
    for k, v in kwargs.items():
        order_summary[k]=v
    return order_summary

class Person():
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def info(self):
        return f"{self.name} - ID: {self.student_id}"
    
class Speaker:
    def play_sound(self):
        return f"Playing Sound."

class Screen:
    def display_image(self):
        return f"Showing image."

class Tablet(Speaker, Screen):
    def tablet_switch(self):
        return f"Tablet is on."
    
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"Meow!"

class Dog(Animal):
    def speak(self):
        return f"Woof!"

class LoginTracker():
    login_count = 0

    def __init__(self):
        LoginTracker.login_count += 1

class Batery():
    def status(self):
        return f"Battery full."

class Laptop():
    def __init__(self):
        self.battery = Batery()
    
    def batery_status(self):
       return self.battery.status()


class SafeBox:
    def __init__(self, code):
        self.__code = code
    
    def unlock(self, attempt):
        if attempt == self.__code:
            return f"Unlocked."
        else:
            return f"Access denied."
    