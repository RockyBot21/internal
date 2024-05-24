#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 00:49:33 2024

@author: user
"""
# =============================================================================
mylist = [True, True, True]
x = all(mylist)
print(x)
# =============================================================================

# =============================================================================
mylist = [False, True, False]
x = any(mylist)
print(x)
# =============================================================================

# =============================================================================
x = ascii('a')
print(x)
# =============================================================================

# =============================================================================
x = 10
print(callable(x))
# =============================================================================

# =============================================================================
x = chr(97)
print(x)
# =============================================================================

# =============================================================================
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
# =============================================================================

# =============================================================================
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)
# =============================================================================

# =============================================================================
class Person:
    name = "John"
    age = 36
    country = "Norway"

x = getattr(Person, 'age')
print(x)
# =============================================================================

# =============================================================================
class Person:
    age = 23
    name = "Adam"

person = Person()

print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))

# Output:
# Person's age: True
# Person's salary: False
# =============================================================================

# =============================================================================
# list of vowels
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))   
print(next(phones_iter))    
print(next(phones_iter))  
# =============================================================================

# =============================================================================
# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
# =============================================================================

# =============================================================================
marks = [65, 71, 68, 74, 61]
# convert list to iterator
iterator_marks = iter(marks)
# =============================================================================

# =============================================================================
# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)
# =============================================================================

# =============================================================================
# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)
# Output: 65
#         71
# =============================================================================

# =============================================================================
string = 'Python'
result = reversed(string)
# convert the iterator to list and print it
print(list(result))
# Output: ['n', 'o', 'h', 't', 'y', 'P']

# creating a list 
cars = ["nano", "swift", "bolero", "BMW"] 
# reversing the list 
reversed_cars = list(reversed(cars)) 
#printing the list 
print(reversed_cars)
# =============================================================================

# =============================================================================
class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

# set value of name to Adam
setattr(person, 'name', 'Adam')
print(person.name)

# set value of marks to 78
setattr(person, 'marks', 78)
print(person.marks)

# Output: Adam
#         78
# =============================================================================

# =============================================================================
String = 'Hello World'
slice_obj = slice(5,11)
print(String[slice_obj])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
# =============================================================================

# =============================================================================
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)
# =============================================================================

# =============================================================================
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)
# =============================================================================

# =============================================================================
class Geeks:
    def __init__(self, name1 = "Arun", num2 = 46, name3 = "Rishab"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3

GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))
# =============================================================================

# =============================================================================
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(x)
# =============================================================================

# =============================================================================
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
# using zip() to map values
mapped = zip(name, roll_no)
print(set(mapped))
# =============================================================================

# =============================================================================
# importing numpy module
# it is equivalent to "import numpy as np"
np = __import__('numpy', globals(), locals(), [], 0)
# array from numpy
a = np.array([1, 2, 3])
# prints the type
print(type(a))


mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))
# =============================================================================

