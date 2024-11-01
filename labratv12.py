Common Mistakes on Assignments 1
Common Mistakes on
Assignments
Day 01 - Printing and Input
Forgetting to convert to a numerical data type
x = input("Enter a number")
print(x+5)
TypeError: can only concatenate str (not "int") to str
# Solution: Convert the input to a numerical data type (float or int)
x = int(input("Enter a number"))
print(x+5)
Forgetting to convert to string 
x=5
print("My number is" + x + ".")
TypeError: can only concatenate str (not "int") to str
#solution: Convert to string
x=5
print("My number is" + str(x) + ".")
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 2
Day 02 - Conditional Statements
Forgetting to add an instruction inside a block of a condition
# WRONG
# implement a program that asks the user to input a number x. 
# If x is smaller than 5 then the program prints x and says "Good Number!"
x = int(input("Number? ")) 
if x < 5:
print(x)
print("Good Number!")
Mistake: In the program above, the second print instruction will always be called. 
# CORRECT: Move instruction to scope of the condition
# implement a program that asks the user to input a number x. 
# If x is smaller than 5 then the program prints x and say "Good Number!"
x = int(input("Number 1? ")) 
if x < 5:
print(x)
 print("Good Number!")
Incorrectly leaving a instruction in a block: 
# WRONG
# implement a program that asks the user to input a number x. 
# If x is smaller than 5 then the program prints x. 
# The program finishes by saying "Good Number!"
x = int(input("Number? ")) 
if x < 5:
print(x)
print("Good Bye!")
In the program above the program only says goodbye if the number is smaller than 5
# SOLUTION: remove the instruction from the scope of the block
# implement a program that asks the user to input a number x. 
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 3
# If x is smaller than 5 then the program prints x. 
# The program finishes by saying "Good Number!"
x = int(input("Number? ")) 
if x < 5:
print(x)
print("Good Bye!")
Day 03 - Sequences and Lists
Assignment of Mutable Objects
#WRONG: Assignment of mutable objects
#Implement a program that proceeds as follows:
#It stores a list [1,2,3] at a variable x
#Then it makes a copy of the list on variable y
#Then it prints both lists
#Then it changes the first element of x to 5, so that the lists are different
x = [1,2,3]
y = x
print(x,y)
x[0]= 5
print(x,y)
Problem: Lists are mutable. By writing y = x, we have that y is a reference to the
same memory location as y. 
#SOLUTION: Copy the mutable object explicitly
#Implement a program that proceeds as follows:
#It stores a list [1,2,3] at a variable x
#Then it makes a copy of the list on variable y
#Then it prints both lists
#Then it changes the first element of x to 5, so that the lists are different
x = [1,2,3]
y = []
for i in x:
y.append(i)
print(x,y)
x[0]= 5
print(x,y)
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 4
A similar problem when constructing matrices
# WRONG
# Implement a program that takes a number n as input and constructs an nxn all-0 matrix
# Then change the entry M[0][0] to 1. 
row = []
for y in range(n):
row.append(0)
print("Row: ",row)
M = [] 
for x in range(n): 
M.append(row)
print("Matrix: ", M)
M[0][0] = 1
print("Changed Matrix: ", M)
MISTAKE: Very subtle. Row is a list. Lists are mutable objects.
The matrix M contains three references to the same location in memory that stores 
the list row. 
# SOLUTION: Move Row = [] inside the loop. In this way, at each iteration a new variable
# is created 
# Implement a program that takes a number n as input and constructs an nxn all-zeros matrix
# Then change the entry M[0][0] to 1. 
n = int(input("Number? "))
M = [] 
for x in range(n):
row = []
for y in range(n):
row.append(0)
M.append(row)
print("Matrix: ", M)
M[0][0] = 1
print("Changed Matrix: ", M)
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 5
Day 04 - Functions
Printing instead of Returning
# FUNCTIONS: 
#WRONG
#Implement a function that takes x and y as input and returns x to the power of y. 
def power1(x,y):
 print(x**y) # printing is not returning. 
z = 5 + power1(2,5) 
print(z)
Error: 
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
Mistake: Since the function is not explicitly returning a value, python assumes that
the function is returning None. Summing 5 with None is not well defined, and the program
casts an error. 
#CORRECT
#Implement a function that takes x and y as input and returns x to the power of y.
def power2(x,y):
 return x**y # now the function is returning a value
z = 5 + power2(2,5) 
print(z)
Returning instead of printing
Sometimes we actually want to implement functions that perform some action, such as
printing a piece of text, but do not return a value.
# WRONG
# Implement a function that takes a string name as input and prints "Hello " + name + "!"
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 6
def Hello(name): 
return("Hello, " + name + "!")
Hello("Anna")
MISTAKE: The function is returning a value instead of printing it. Therefore, when we 
call the function nothing happens. 
# CORRECT
# Implement a function that takes a string name as input and prints "Hello " + name + "!" 
def Hello(name): 
print("Hello, " + name + "!")
Hello("Anna")
Returning before a computation is complete
# WRONG
# Implement a function that takes a number n as input and returns the sum of the numbers
# 1,2,...,n
def sum(n):
s = 0
for i in range(1,n+1): 
s = s+i
return s
print(sum(5))
print(sum(6))
Mistake: The instruction `return s` was wrongly placed inside the for loop.
It will return the value of s after the first iteration. That is, the function will
always return 1 in this case. 
#SOLUTION: Return the value after the for loop has been completed. 
# Implement a function that takes a number n as input and returns the sum of the numbers
# 1,2,...,n
def sum(n):
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 7
s = 0
for i in range(1,n+1): 
s = s+i
return s
print(sum(5))
print(sum(6))
Day 06 - Classes
Not many mistakes in this day strictly related to classes. Most problems during this day
were related to conditional statements, and to functions. 
Day 07 - Sets and Dictionaries
One common mistake was to initialize the empty set as {} . This is not the empty set,
but rather the empty dictionary. The empty set is denoted by set() . 
Day 08 - Files
Not using the parameter
This was a very common mistake in the Day 08 - Files. The task was to implement a
function that takes a string filename as input and creates a file whose name is the string
stored in filename . As an example I stated that if the file was called “Example.txt” the
function should create the file “Example.txt”. Many students hard-coded the string
“Example.txt” in their read/create functions. This is clearly wrong since in this way the
functions can only read/create the file “Example.txt” instead of being able to create the
file whose name is passed as a parameter. 
# Wrong 
def createFile(filename):
file = open("Example.txt",w)
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Common Mistakes on Assignments 8
MISTAKE: In this code the file to be created will always be called "Example.txt". 
What you want is to create a file whose name is same as the string passed as parameter.
# CORRECT: Use the parameter passed to the function, not the example. 
def createFile(filename):
file = open(filename,w)
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only