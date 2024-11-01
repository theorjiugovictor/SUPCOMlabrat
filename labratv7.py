#Defining Functions Functions are used to encapsulate code that may be used in several places of a program. Intuitively, a function takes a collection of parameters as input, and executes a sequence of instructions that may depend on the parameters. In python, functions are defined using the keyword def.
def hello(name):
    print("Hello, " + name + "!")
    print("How are you doing?")

print("Printing some Greetings: ")
hello("Bob")
hello("Alice")

#A function that computes the mean of three numbers.
def Mean(x1, x2, x3):
    return (x1 + x2 + x3) / 3.0

print(str(Mean(4, 5, 12)))
print(str(Mean(10, 3, 13)))

#This function computes the inner product of two lists of integers. For simplicity, we assume that the lists passed as input has the same length
#assume x and y are lists of integers of same length
def InnerProduct(x, y):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i] * y[i]
    return sum
x = [3, 2, 1, 2]
y = [-1, 2, 3, 2]
print(InnerProduct(x, y))