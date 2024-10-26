################################
################################
## To activate the code in one section, 
## comment the two lines with triple quotation 
## marks """, one before and one after the code.
########## Priting #############
"""
print("Hello, User!") 
"""
########## Printing Several Lines #############
""" 
print("Hello, User!")
print("What is your name? ")
"""
########## Input vs Print #############
""" 
name = input("What is your name? ")
print("Your name is " + name) 
"""

########### int vs float  ############

# int is used for integers: 0,1,2,3... -1,-2,-3...
# Age, number of days, number of participants, etc.

""" 
age = int(input("What is your age? "))
print("Your age is " + str(age) + ".") 
"""

# float is used for numbers with decimals
# temperature, averages, etc. 

"""
temp = float(input("What is your temperature? "))
print("Your temperature is " + str(temp) + ".") 
"""

# Obs: if the program expects an int and the user 
# replies with a float, we have an error. On the other
# hand, if the program expects a float, the user can 
# answer with a string encoding an int, and it will 
# be automatically converted to float

# Question: If we want the user to answer in the 
# next line? 
# Answer: add a \n at the end of the string
"""
temp = float(input("What is your temperature?\n"))
print("Your temperature is " + str(temp) + ".")
"""

# Calculator Type programs
# Ask the user to input some numbers. 
# Then compute some formula

"""
number1 = float(input("Number 1? "))
number2 = float(input("Number 2? "))
print(str(number1) + " multiplied by " + str(number2) +  " is equal to " + str(number1*number2)) 
"""

# Operators

# +, *, - , / are the usual 
# addition, multiplication, subtraction, division


# % : Modular arithmetic operator
# Important to test if a number is even or odd: 
# x is even if x % 2 is equal to 0
# x is odd if x % 2 is equal to 1

""" 
print(56 % 2)
print(57 % 2)
"""
# % Can also be used to test is a number is divisible 
# by another numbers (ex: 3)
"""
print(66 % 3)
print(67 % 3)
print(68 % 3) 
"""

# // : Integer division 

"""
print(34.5 / 2 ) # Division with decimals
print(34.5 // 2 ) # Division and rounding to integer
"""

# Printing with the end parameter 
# The end paramter specifies what the program 
# will print after it has printed the "main" string 
# By default, this parameter is set to "\n" (new line)
# But it can be any string. Typical uses: 
# the empty string "", a whitespace " ", a dash "-". 
# This parameter will be more useful later, when 
# using loops. 

""" 
print("The book is on the table.", end = "\n")
print("The sky is blue.", end = "\n")
"""

"""
print("The book is on the table.", end = " ")
print("The sky is blue.", end = " ")
"""


# Scope
# This notion will be mostly relevant when we
# learn about functions (Day 04). 
# Intuitively, the scope of a variable is the
# portion of the program where a variable is visible

# Global scope (Defined at identation level 0)
offset = 10

# Local cope. Defined within a function. 
# Visible only within the function. 
# variables x and y of function addition
def add_with_offset(x,y): 
    return x + y + offset

# Variables x and y of function mult. 
# Not the same variables as x and y of 
# the previous function.
def mult_with_offset(x,y): 
    return x*y + offset

print("Add plus offset:",add_with_offset(6,8))
print("Mult plus offset:",mult_with_offset(5,6))