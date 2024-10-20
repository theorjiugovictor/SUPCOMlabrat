# Calculating the Area of a rectangle
# We use the input function stored in variables (width & Length) but want the user input to be a numerical data type "float"
length = float (input("Type the Length of the rectangle?"))
width = float (input("Type the Width of the rectangle?"))

Area = (length * width)
print("The Area of the Rectangle is", Area)

#calculating the Average of three Numbers
first_digit = float(input("Type the first digit:"))
second_digit = float(input("Type the second digit:"))
third_digit = float(input("Type the third digit:"))

Average = (first_digit + second_digit + third_digit)/(3)

print("This is the average of three number", round (Average, 2))

# Additon (+), Subtraction (-), Multiplication (*), Division (/), Floor Division (//), Modulus (%), Exponentiation (**)
a = 16
b = 3
print("Addition:", 16 + 3)
print("Subtraction:", 16 - 3)
print("Division:", 16/3)
print("Multiplication:", 16*3)
print("floor division:", 16//3)
print("Modulus:", 16%3)
print("Exponential:", 16**3)

#Computing the norm of a 2D Vector (x,y) = Square root(X^2 + Y^2). This requires you to import the library
#import the math module, which is a module that contains a wide variety of useful functions such as square root function, the floor and ceil functions, trigonometric functions, logarithmic functions, etc.
import math
x = float(input("Coordinate of X = "))
y = float(input("Coordinate of Y = "))
norm = math.sqrt(x**2 + y**2)
print("Norm of (x,y) =", norm)

#Math Module Basic Constants
#math.pi is an approximation of the number pi , that is, 3.1415... while math.e is an approximation of the Euler’s number, that is, the number 2.7182... .
c = math.e
d = 144
e = 2
print("pi:", math.pi)
print("e:", math.e)
print(c)
print("floor(c):", math.floor(c))
print("ceil(c):", math.ceil(c))
print

#Math Module Square Root
print("Square Root of D: ", math.sqrt(d))
print("log(c,d):", math.log(c,d))
print("sin(d):", math.sin(d))
print("cos(d)", math.cos(d))
print("tan(d)", math.tan(d))

#An alternative way of creating a new line is to use the new line character \n within a print command.
#For split texts in different print commands, we used end = "" to join them together
print("The value of Eulers number is", end = "")
print(x, end = "")
print(".")
print("These are digits", c,d,e, sep=" - ")

#F-strings provide a convenient way to embed python expressions within strings. This is useful for example when we want to print strings that mix text with the values of variables. F-strings are formed by an f followed by a string within quotation marks. Expressions are embedded in f-strings using curly brackets {} .
name = "John" 
age = 30 
print(f"Passenger {name} is {age} years old.")

#In f-strings, a colon ( : ) is used to introduce formatting specifications that control parameters such as the number of decimal places for floats, the width of a field, alignment, etc.
pi = 3.141592653589793 
print(f"Pi to 4 decimal places: {pi:.4f}")
precision = 5 
print(f"Pi to {precision} decimal places: {pi:.{precision}f}")

#Width of a field and text alignment
number = 1234 
print(f"|{number:>10}|") # right-aligned in a field of width 10 
print(f"|{number:^10}|") # centered in a field of width 10 
print(f"|{number:<10}|") # left-aligned in a field of width 10

width = 16 
print(f"|{number:>{width}}|") # right-aligned in a field of width 10 
print(f"|{number:^{width}}|") # centered in a field of width 10 
print(f"|{number:<{width}}|") # left-aligned in a field of width 10

#Padding Numbers with leading zeroes
x = 123 
y = 45678 
print(f"{x:010}") 
print(f"{y:010}")

#An identifier is in the local scope of a function if it is defined within that function. Thisdefinition is only valid within the function, not outside of it. For example, below we definea function sum(x,y) that sums the values of variables x and y . This function uses anauxiliary variable z to store the result of the sum. Subsequently it returns z . In thiscontext, the identifier z is in the local scope of the function sum and cannot be accessed outside this function.

def sum(x,y): 
    z = x + y
    return z

def mult(x,y): 
    z = x * y
    return z

x=10
y=5
print(f"{x} + {y} = {sum(x,y)}.")
print(f"{x} * {y} = {mult(x,y)}.")

