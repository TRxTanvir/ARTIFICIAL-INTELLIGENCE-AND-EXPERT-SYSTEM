# -*- coding: utf-8 -*-
"""21-45590-3 Lab 02 Basic_Python_Statements,_IO_and_Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ddYx1eJnO-nsvy9Ar-TGz1gFuSxDplZq

# About this notebook
<p style="text-align: justify"> Here, you will learn the basic statements of python and function. Some codes will be given for demonstration. Some other codes, you will do as excercise.</p>

## Submission
<p style="text-align: justify">After completing the practice codes and exercises, download the notebook (.pynb file) and submit the notebook  to MS Teams inbox in the class period</p>
<p> 1.<b> You must submit your own code</b>. If similarity found negative marking will be given.</p>
<p> 2. Modify the file name writing your ID at the beigining of the file name.</p><p> <b>Example: 21-45590-3 Lab 02.ipynb</b></p>
<p> 3. Other file format (except .pynb) or link will not be accepted.</p>

# User Input
"""

a = 21
print(a)

a = input()
print(a)
print(type(a))

a = input('Enter a value: ') # always returns string
print('The given value is '+ a)
print(type(a))

a = int(input('Enter a number: ')) # returns string but converted to int
print(f'The result is {a+15}')
print(type(a))

while True:
  a = input('Enter your Birth Year:')
  if a.isdigit():
    print(f'You are {2024-int(a)} years old')
    break
  print('WRONG INPUT')

#classexercise
import datetime

while True:
    birth_year_str = input('Enter your Birth Year: ')
    birth_month_str = input('Enter your Birth Month (1-12): ')
    birth_day_str = input('Enter your Birth Day (1-31): ')

    if birth_year_str.isdigit() and birth_month_str.isdigit() and birth_day_str.isdigit():
        birth_year = int(birth_year_str)
        birth_month = int(birth_month_str)
        birth_day = int(birth_day_str)

        if birth_year > 0 and 1 <= birth_month <= 12 and 1 <= birth_day <= 31:
            today = datetime.date.today()
            birthdate = datetime.date(birth_year, birth_month, birth_day)
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

            print(f'You are {age} years old')

            break
        else:
            print('WRONG INPUT: Invalid date values.')
    else:
        print('WRONG INPUT: Please enter numeric values.')

"""# if statement
There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’
"""

# indent
i = 2
if i < 5: # () not required, {} not required
  print('okay')
  print('fine')
else:
  print('bad')
print('not okay') # will be executed in each run

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
  print('More')

"""<b>Exercise 1:</b> Input a course mark (0-100) from user and use the <b>if</b> statement to print corresponding grade."""

# code here
mark = int(input("Enter your course mark (0-100): "))
if mark > 100 or mark < 0:
    print("Invalid input. Please enter a number between 0 and 100.")
elif mark == 100:
    print("Grade: A+ - Perfect Score!")
if mark >=90  <100:
    print("Grade: A+")
elif mark >= 85:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B+")
elif mark >= 75:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C+")
elif mark >= 65:
    print("Grade: C")
elif mark >= 60:
    print("Grade: D+")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")
if mark < 0:
    print('Negative changed to zero')

"""# for statement
<p style="text-align: justify">The for statement in Python differs a bit from what you may be used to in C or C++. Rather than always giving the user the ability to define both the iteration step and halting condition, Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.</p>
"""

# Measure some strings:
words = ['cat', 'window', 'dhaka','ctg']

for w in words:
    print('the word is:{}'.format(w))

list(range(4))

list(range(1,20))

list(range(4,10,2))

words = ['cat', 'window', 'dhaka','ctg','ABC']
for i in range(len(words)):
    print('the word is: {}'.format(words[i]))

"""### The range() Function
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
"""

list(range(3,10,2))

numbers = [1, 56, 78, 8,7]

for n in numbers:
    print(n+10)

list(range(5))

# repeated for 0 to 4
# for(i=0;i<5;i++)
for i in range(0,20,2):
    print(i)

"""<p style="text-align: justify">The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):</p>"""

list(range(5, 10))

list(range(0, 10, 3))

list(range(10, 2, -1))

list(range(-10, -101, -30))

for i in range(len(numbers)):
    print(i, numbers[i])

for i in range(2,100,5):
    print(i,end=',')

"""<b>Exercise 2:</b> Print all the even numbers between 0 to 100 using <b>for loop</b> and <b>range</b>."""

# code here
for i in range(0, 101, 2):
    print(i, end=" ")
    i = 0

country = "bangladesh"
for c in country:
    print(c,end=' ')

"""# Functions
<p style="text-align: justify">The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.</p>
"""

from math import sqrt

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

# Check if a few numbers are prime
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in numbers:
  if is_prime(num):
    print(f'{num} is a prime')
  else:
    print(f'{num} is not a prime')

def fib(n):    # write Fibonacci series up to n
    lst = [0,1]
    a, b = 0, 1
    while True:
        #print(a, end=' ')
        a, b = b, a+b
        if b < n:
          lst.append(b)
        else:
          break
        #print()
    return lst

# Now call the function we just defined:
r = fib(1000)
print(r)

# define method
def addnumbers(a, b): # add numbers and return result
    # logic
    c = a + b
    return c

addnumbers(2,33)

y = addnumbers('8ppp', '  9') # use or call method
print(y)

addnumbers([33,77], [66])

# add list values
def addValues(num):
    sum = 0
    for n in num:
        sum = sum+ n
    return sum

addValues(range(10))

addValues([])

v = [5, 4,12, 7]
addValues(v)



v = [5, 4,12, 7, 5, 4,12, 7, 5, 4,12, 7]
addValues(v)

# method/function
def multiTable(n, r=10):
    for i in range(1,r+1):
        print("{}x{}={}".format(n,i,n*i))

multiTable(8)

multiTable(15)

"""<b>Exercise 3:</b> Define a <b>method/function</b> which will take two lists of numbers and returns a list (sum of two lists)
<p>Example:<br>
    Input: [3,4,5,1] and [6,7,2,8]<br>
    output: [9,11,7,9]</p>

"""

def add_lists(list1, list2):

  result = []
  for i in range(min(len(list1), len(list2))):
    result.append(list1[i] + list2[i])
  return result

# Get user input for the lists
list1_str = input("Enter the first list of numbers (separated by spaces): ")
list2_str = input("Enter the second list of numbers (separated by spaces): ")

# Convert the input strings to lists of numbers
list1 = [int(x) for x in list1_str.split()]
list2 = [int(x) for x in list2_str.split()]

# Calculate and print the sum of the lists
sum_list = add_lists(list1, list2)
print("Sum of the lists:", sum_list)

"""<b> Exercise 4:</b> Write a <b>method</b> which will take the <b>full name</b> as input and return both the first name and last name.
<p>Example:<br>
    Input: Arafat Rahman Sunny<br>
    Output: First name: Arafat, Last name: Sunny</p>
"""

def get_first_last_name(full_name):
  names = full_name.split()
  first_name = names[0]
  last_name = names[-1]  # Use -1 to get the last element
  return first_name, last_name

# Get user input for the full name
full_name = input("Enter your full name: ")

# Extract and print the first and last names
first_name, last_name = get_first_last_name(full_name)
print(f"First name: {first_name}, Last name: {last_name}")

"""# Output Formatting (Optional)
Go to the [link](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) and practice the codes below.

# ***1***
"""

# code here

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

"""# ***2***"""

yes_votes =10000
total_votes = 44444
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

"""# ***3***"""

s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

"""# **4**"""

import math
print(f'The value of pi is approximately {math.pi:.3f}.')

"""# *5*"""

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

"""# ***6***"""

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

"""7"""

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

"""8"""

print('We are the {} who say "{}!"'.format('GenZ', 'NewBD'))

"""9"""

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

"""10"""

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

"""11"""

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

"""12"""