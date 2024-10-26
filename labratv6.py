#For loops with ranges 
#To repeat a given block of code for a specific number of times, we use for loops with ranges. 

for x in range(4):
 print(x)

#print the first 5 rows of the function table of the function x squared, that is x**2
for x in range(5):
 y = x**2
 print(x,y)

#specify a number of rows to be plotted. This number is then used to set the size of the range. range range(n_points) is a representation of the sequence of numbers from 0 to n_points-1
n_points = int(input("Number of points? "))
for x in range(n_points):
 y = x**2
 print(x,y)

 # iterate over a sequence of elements starting at an integer a and ending at an integer b , then we may use the construction range(a,b+1) . Note the +1 in the second argument. 
a = int(input("First point? "))
b = int(input("Last point? "))
for x in range(a,b+1):
 y = x**2
 print(x,y)

#for' loops to iterate through each element in a list, executing a block of code during each iteration, which can utilize the current element being processed. In the next example we show how to iterate through a list, printing at each iteration one element from the list. Note that lists are traversed from left to right.
students = ["Alice","Bob","Carla"]
for student in students:
    print(student)

#incremental update of value
#create a list of names of students, where each name is provided by the user. We start by asking the user the number of names to be read, and then create a variable student that stores an empty list. At each iteration of the loop, the program asks the user to input the name of a student and appends this name to the list. Once this is done, the program prints the list.
n_students = int(input("Number of Students? "))
list_students = []
for x in range(n_students):
 student = input("Student Name? ")
list_students.append(student)
for student in list_students:
 print(student)

#explicit example of this phenomenon. First, we ask the user to enter a list of numbers. Then, once the list has been entered, the program will calculate the sum of these numbers. This is done by creating a variable sum that will be iteratively updated while we traverse the list. At the beginning, the value of sum is set to 0 . Then, at each step the for loop adds to this sum the value of the element currently being iterated. At the end, when all elements have been processed, the variable sum will hold the value of the final sum.
 # Constructing a list of numbers
size_list = int(input("Size of the list? "))
list_numbers = []
for x in range(size_list):
 number = int(input("Number? "))
 list_numbers.append(number)
print("\nList:", list_numbers,"\n")
# Summing the elements in the list
sum = 0
print("Initial sum: ",sum)
for number in list_numbers:
 sum = sum + number
 print("Sum after adding " + str(number) + ": " + str(sum))
print("Final Sum:", sum)

#In the next example we show how to use for loops to filter elements from a list. More specifically, the following code show how to select the even numbers from a list of numbers.
list_numbers = [1,3,2,4,5,7,2,8]
even_list = [] 
for number in list_numbers: 
    if (number % 2 == 0): 
     even_list.append(number)
print("Original List:",list_numbers)
print("Filtered List:",even_list)

#how to concatenate all names in a list of strings.
strings = ["Red", "Green", "Blue", "Yellow"]
big_string = ""
for string in strings:
    big_string = big_string + string
print(big_string)

#The length of a list A can be obtained using len(A) . Knowing the length of a list is useful when we want to iterate though its elements using indices. For example, when we want to iterate through two equal-sized lists at the same time, it is convenient to use indices. The following code use this method to construct a list C where each entry C[i] is the sum of the entries A[i] and B[i] of lists A and B .
# Assumes the lists A and B have the same size 
A = [2,4,6,8,10]
B = [3,6,9,12,15]
C = []
for i in range(len(A)):
    C.append(A[i]+B[i])
print(A)
print(B)
print(C)

#For loops are used to define loops that iterate over ranges, lists, strings or tuples. In all these cases, the number of iterations to be performed is known in advance before the execution of the loop. In many cases however, we may need to define loops that run for a number of iterations that is not necessarily known before the start of the loop. For this, we the while loop construction:
exit = False
names = []
while not exit:
    x = input("Enter a name: ")
    if x == "exit":
        exit = True
    else:
        names.append(x)
print(names)

#Another way to stop a loop is using the command break . For example the following construction simulates the do-until construction available in other languages. More specifically, in this construction, <Block of code> is executed until <Condition> is satisfied
#Use of this construction by implementing a loop that iterates through the elements of a list until the first number which is divisible by both of 3 and 5 is found.
list_numbers = [12, 18, 21, 28, 15, 42, 56]
index = 0
while True:
 if list_numbers[index] % 3 == 0 and list_numbers[index] % 5 == 0:
    print(f"The first number divisible by 3 and 5 is {list_numbers[index]}.")
 break
 index += 1

#Nested Loops are loops inside loops.
#Nested Loops for cartesian products of sequences. 
for x in range(3):
 for y in range(3):
  print(x,y)

#Here, both variables x iterates through the range 0,1,2 . At the first iteration of the outer for loop, variable x is set to value 0 . While the variable y is successively set to the values 0 , 1 and 2 . As an effect, we have that the pairs 0 0 , 0 1 , and 0 2 are printed. Subsequently, in the next iteration of the outer for loop, variable x is set to value 1 , and pairs 1 0 , 1 1 , and 1 2 are printed. Finally, variable x is set to 2 and the pairs 2 0 , 2 1 and 2 2 are printed. In our next example, we use nested for loops to iterate over pairs of elements, where the first coordinate belong to a list of fruits and the second belongs to a list of colors.
fruits = ["apple","orange","strawberry"]
colors = ["green","red"]
for fruit in fruits:
    for color in colors:
        print(f"{fruit:12} {color:12}") 

#Generating a Multiplication Table
#In the next example, we use nested loops to implement a program that asks the user to input a number number and then generates a multiplication table whose rows and columns are indexed by the numbers from 1 to number . This example shows more explicitly how the variables used to iterate through indices can be involved in the computation that occurs in the block of code of the inner most loop
number = int(input("Number? ")) 
for i in range(1, number+1):
 for j in range(1, number+1):
  print(i,"x",j,"=",i*j)
 print("----------")

#A similar example shows how to use indices to iterate through lists. In this example, we are given two lists A and B and the goal is to use nested loops to operate with the i -th element of list A with the j -th element of list B . Note that in this example we are not computing the multiplication i*j , but rather the multiplication A[i]*B[j] .
A = [3,5,8,4] 
B = [9,3,2] 
print("A = ", A)
print("B = ", B)
print()
for i in range(len(A)):
 for j in range(len(B)):
    print("A[" + str(i) + "] x B[" + str(j) + "] = " + str(A[i]*B[j]))
 print("----------")

 #Traversing a matrix
 #Matrices in Python are represented as lists of lists, where the inner lists have all the same size. The i -th inner list represents the i -th row of the matrix. The next example shows how to iterate through the entries of a matrix. We use a variable row to iterate trough each row of the matrix, and a variable x to iterate through each element of row. Then, we run a block of code that may depend on x such as printing x .
 matrix = [
 [2, 1, 3, 1], # row 0
 [4, 5, 2, 3], # row 1
 [7, 1, 6, 8] # row 2
]
for row in matrix:
 for x in row:
    print(x, end=" ")
 print()

 #The next example shows how nested loops can be used to find common elements in two lists A and B . For each element x in the list A , the program runs through each element y of list B and tests whether x==y . If this is the case, the program states that x is a common element. Otherwise, it just moves to the next iteration.
 A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
for x in A:
 for y in B:
     if x == y:
        print(f"Common element: {x}")

#Constructing a Matrix of All Zeros
n = int(input("Number? "))
M = [] 
for x in range(n):
    row = []
    for y in range(n):
        row.append(0)
    M.append(row)
print("Matrix: ", M)

#Constructing a Matrix whose Entries Depend on the Indices The previous code can be easily modified in order to construct matrices where each entry M[x][y] is equal to the value of a function f(x,y) for some given function f . For example suppose that we want entry M[x][y] to be the value x**2 + y**2 . Then, in this case, all we need to do is to replace the instruction row.append(0) , within the scope of the second for loop, by the instruction row.append(x**2+y**2)
n = int(input("Number? "))
M = [] 
for x in range(n):
    row = []
for y in range(n):
    row.append(x**2+y**2)
M.append(row)
print("Matrix: ", M)

#: Building an Agenda. In the next example, we show how to use nested for loops to implement a program that asks the user to input their agenda for the week. We assume for simplicity that we want to specify our activities only for Monday, Tuesday and Wednesday, and that each day is split into four activities, to be specified on each hour between 08:00-12:00
days = ["Monday","Tuesday","Wednesday"]
times = ["08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00"]
agenda = []
for x in range(len(days)):
    print(f"Enter plan for {days[x]}:")
plan = []
for y in times:
    activity = input(f"Activity for time {y}? ")
plan.append(activity)
print()
agenda.append(plan)
print("\n------------------- AGENDA -------------------\n")
for x in range(len(days)):
    print(f"{days[x]}:")
for y in range(len(times)): 
        print(f"{times[y]}: {agenda[x][y]}" )
print()

#Going to the Super Market. Nesting a While Loop inside a For loop. Next, we provide an example of how distinct types of loops can be nested within each other. More specifically, in this example the outer loop is a for loop and the inner loop is a while loop. Our goal is to implement a program that keeps a record of items bought by the user in a supermarket during a usual week. This record is stored in a list of lists called all_items . Note that this is not a matrix because the inner lists may have distinct sizes.  For simplicity, we assume that the user is going to the supermarket on Monday, Wednesday and Friday, and for this reason, we use a for loop to iterate through these days. On each day, our program builds a list basket of items that have been selected in that day, and then appends this list to the record all_items . To construct the the basket list on the other hand, we use a while loop, since we do not know in advance how many items the user will buy in that day. In the while loop, the program asks the user to input one item at a time. Once the user replies with "exit" the basket is considered to be full and the while loop halts, giving rise to another iteration of the for loop.
days = ["Monday","Wednesday","Friday"] 
all_items = []
for x in range(len(days)): 
 print(f"\n{days[x]}: Select items. Answer 'exit' when you are ready.\n")
 basket = []
 while True:
    item = input("Pick an item: ")
    if item == "exit":
        break 
    else: 
        basket.append(item) 
 print(f"Items bought on {days[x]}: {basket}")
 all_items.append(basket)
print("\n--------------- Buying Record ---------------\n")
for x in range(len(all_items)): 
    print(f"{days[x]}: ",end = "")
    for y in range(len(all_items[x])):
        if y == len(all_items[x])-1:
            end_str = "\n"
        else:
            end_str = ", "
        print(all_items[x][y],end = end_str)

#Once the record all_items has been constructed, it is time to display it in the screen.For this purpose, we use a nested for loop. The outer for loop iterates through the range len(all_items) using a variable x , while the inner for loop iterates over the range len(all_items[x]) using a variable y . Note that the length of the range in the second for loop varies from day to day, since the size of the list of items may vary from one day to another.

#Lists are objects that are used to store sequences of other objects. Lists are created using brackets. The most basic list is the empty list, which contains no object.
EmptyList = []
print("Empty list: ", EmptyList)

#One can also create a list initialized with a certain number of elements. For instance, below we have a list of pets.
pets = ["dog", "cat", "hamster", "fish"]
print(pets)

#Lists may contain repeated elements.
pets = ["dog", "dog", "hamster", "fish"]
print(pets)

#Lists may also contain elements of distinct types.
crazyList = ["cat", 10, 2.71]
print(crazyList)

#To obtain the number of elements in a list, use the function len() .
pets = ["dog", "cat", "hamster", "fish"]
print(len(pets))

#Specific objects in a list may be accessed using an index. In a list with n elements, positive indexes vary between 0 and n-1 . In order to retrieve the i -th element of a list, write [i] after the name of the list.
pets = ["dog", "cat", "hamster", "fish"]
#The index of the first element of the list is 0
print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])

#Indices can also be negative. The index -1 accesses the last element, -2 the penultimate element, and so on.
pets = ["dog", "cat", "hamster", "fish"]
#The index of the first element of the list is 0
print(pets[-1])
print(pets[-2])
print(pets[-3])
print(pets[-4])

#If one tries to retrieve an element whose index is greater than the length of the list minus one, or smaller than the negative of the length of the list, an error occurs.
pets = ["dog", "cat", "hamster", "fish"]
print(pets[4])
#Same error with print(pets[-5])
IndexError: list index out of range

#The elements of a list may be modified. For instance, to modify the 3-rd element of the list, just assign a new value to the element with index 2 (recall that the first element of the list has index 0).
pets = ["dog", "cat", "hamster", "fish"]
print(pets)
pets[2] = "guinea pig"
print(pets)

#One can also replace a sub-list by another list. In the fallowing example we replace the sub-list consisting of ["cat","hamster"] with the list ["lion","capybara","shark"] .
pets = ["dog", "cat", "hamster", "fish"]
print(pets)
pets[1:3] = ["lion","capybara","shark"]
print(pets)

#To insert a new element at the end of the list, use the function append() . To insert an element at a specific position, use the function insert() . More specifically, append(x) inserts element x at the end of the list, while insert(i,x) inserts element x at position with index i .
pets = ["dog", "cat", "hamster", "fish"]
print(pets)
pets.append("platypus")
print(pets)
pets.insert(2,"aligator")
print(pets)