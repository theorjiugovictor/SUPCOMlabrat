#The simplest form of conditional statement in python is the if statement. if <Condition>: <Block of code>
price = int(input("What is the price of the item? ")) 
if price <= 1000:
    print("Great!")
    print("We buy it!")
print("Have a nice day!")


price = int(input("What is the price of the item? ")) 
if price <= 1000: 
 print("Great!") 
 print("We buy it!") 
else: 
 print("Too expensive!") 
 print("We buy it somewhere else.") 
print("Have a nice day!")

age = int(input("Age .of the passenger? ")) 
if age <= 11: 
 print("Child ticket") 
 price = 0 
elif age >= 12 and age <= 17: 
 print("Teenager ticket") 
 price = 1 
elif age >= 18 and age <= 65: 
 print("Full Ticket") 
 price = 2 
else: 
 print("Senior ticket.")
 price=1.5 
print("Price: ", price)

#COMPARISON OPERATORS
#If we want to compare the value of two objects in Python, we need to use the equality comparison operator == . For example, x == 5 tells Python to test whether the value of variable x is equal to 5 while x == y tests whether the value assigned to variable x is equal to the value assigned to variable y . The result of this test is a Boolean value, that is to say, True if the equality holds and False otherwise. Note that the operator == does not modify the value of variable x .
x = 5 # Assigns value 5 to variable x 
y = x # Assigns the value of x to variable y 
z = 6 # Assigns the value 6 to variable z 
# Printing the result of equality testing 
print(x == 5) 
print(x == y) 
print(x == z)

#Python has also an inequality operator != , which returns True if the values of the operands are not equal and False if they are equal. In this sense, x != y returns True if the value assigned to x is not equal to the value assigned to y and returns False otherwise.
x = 5 # Assigns value 5 to variable x 
y = x # Assigns the value of x to variable y
z = 6 # Assigns the value 6 to variable z 
# Printing the result of inequality testing 
print(x != 5) 
print(x != y) 
print(x != z)

#The operators > , < , >= and <= are used to test whether an object is greater than, smaller than, greater than or equal, and smaller than or equal to another object, respectively
x = 5 
y = 6 
print(x<y) 
print(x>y) 
print(x<=x) 
print(x>=y)

x = int(input("Enter a number: ")) 
if x == 7: 
 print("You entered the magic number!") 
print("Have a nice day!")

#Validating password
password = input("Enter the password: ") 
if password == "MyBirthday": 
 print("Welcome to the Machine.") 
else: 
 print("The password is incorrect.")

#Inequality operator in s conditional statement
X = float(input("X: ")) 
Y = float(input("Y: ")) 
if Y != 0: 
    print("X divided by Y:", X/Y)
else: 
 print("Error: division by zero.")

#Greater than or Equal Operator
age = int(input("Age? ")) 
if age >= 21: 
 print("Welcome to the Monopoly.") 
else: 
 print("Age restricted area.")

 #Less than or equal operator
 x = int(input("How fast did you drive? ")) 
if x <= 110: 
 print("This is within the speed limits.") 
print("No further questions.")


#Boolean Operator such as and , or and not are used to define Boolean expressions in terms of simpler Boolean expressions
#AND Operator
age = int(input("Age? ")) 
has_license = input("License? (Yes/No) ") 
if age >= 18 and has_license=="Yes": 
 print("You are allowed to drive.") 
else: 
 print("You are not allowed to drive.")

#Checking if a number is inside a valid range
number = int(input("Number? ")) 
if number > 0 and number < 100: 
 print("Number inside valid range.")