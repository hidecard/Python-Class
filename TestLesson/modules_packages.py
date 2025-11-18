# Modules and Packages in Python
# User-defined module and usage of standard modules: os, sys, datetime, json, calendar, random, math, collections

import os
import sys
import datetime
import json
import calendar
import random
import math
from collections import Counter, defaultdict

# User-defined module (this file itself can be imported, but for demo, we'll define functions here)
def user_defined_function():
    """A simple user-defined function."""
    return "Hello from user-defined module!"

class UserDefinedClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Standard Modules Usage
def os_module_examples():
    print("OS Module:")
    print("Current directory:", os.getcwd())
    print("List files:", os.listdir('.'))
    print("Path exists:", os.path.exists('example.txt'))

def sys_module_examples():
    print("SYS Module:")
    print("Python version:", sys.version)
    print("Platform:", sys.platform)
    print("Command line args:", sys.argv)

def datetime_module_examples():
    print("Datetime Module:")
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

def json_module_examples():
    print("JSON Module:")
    data = {'key': 'value', 'number': 42}
    json_str = json.dumps(data)
    print("JSON string:", json_str)
    parsed = json.loads(json_str)
    print("Parsed back:", parsed)

def calendar_module_examples():
    print("Calendar Module:")
    print("Calendar for 2023:")
    print(calendar.calendar(2023))

def random_module_examples():
    print("Random Module:")
    print("Random integer:", random.randint(1, 10))
    print("Random choice:", random.choice(['apple', 'banana', 'cherry']))

def math_module_examples():
    print("Math Module:")
    print("Square root of 16:", math.sqrt(16))
    print("Pi value:", math.pi)
    print("Factorial of 5:", math.factorial(5))

def collections_module_examples():
    print("Collections Module:")
    # Counter
    list_items = ['a', 'b', 'a', 'c', 'b', 'a']
    counter = Counter(list_items)
    print("Counter:", counter)

    # defaultdict
    dd = defaultdict(int)
    dd['key1'] += 1
    dd['key2'] += 2
    print("Defaultdict:", dict(dd))

# Main execution
if __name__ == "__main__":
    print("User-defined function:", user_defined_function())
    obj = UserDefinedClass("Alice")
    print("User-defined class:", obj.greet())

    print("\n" + "="*50)
    os_module_examples()
    print("\n" + "="*50)
    sys_module_examples()
    print("\n" + "="*50)
    datetime_module_examples()
    print("\n" + "="*50)
    json_module_examples()
    print("\n" + "="*50)
    calendar_module_examples()
    print("\n" + "="*50)
    random_module_examples()
    print("\n" + "="*50)
    math_module_examples()
    print("\n" + "="*50)
    collections_module_examples()
