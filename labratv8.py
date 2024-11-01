#Sets are data structures used to store collections of objects. In contrast with lists, the elements of a set cannot be retrieved using indexes. Nevertheless, one can still insert and remove elements, as well as test for membership. A set is created by listing its elements within curly brackets.
s = {5,2,7} #set
print(s)
{2, 5, 7}

#The empty set is denoted by set() . Note that {} is not the empty set, but rather the empty dictionary (see section Dictionary). 
s = set()
print(s)
set()

#The number of elements in a set s can be retrieved using len(s) .
s = {5,2,7}
print(len(s)) #number of elements of the set
3

#To test whether a given element x belongs to a set S , we use the construction x in S .
x = 5
y = 8
s = {5,2,7}
print(x in s)
print(y in s)
True
False

#To add elements to a set, we use the method add .
s = {5,2,7}
print(s)
s.add(4) #add element
print(s)
{2, 5, 7}
{2, 4, 5, 7}
Elements can be removed from a set using the method remove.
s = {5,2,7}
print(s)
s.remove(5) #remove element
print(s)
{2, 5, 7}
{2, 7}
#Below we show how the Boolean operations union, intersection, set difference and symmetric difference are implemented. Note the s.operation(t) returns a new set corresponding to the result of operating s with t . Therefore, both sets s and t remain intact.
s = {5,2,7}
t = {"a","b",7,2}
print("s: ",s)
print("t: ",t)
print("Union: ",s.union(t))
print("Intersection: ",s.intersection(t))
print("Difference: ",s.difference(t))
print("Symmetric Difference: ",s.symmetric_difference(t))
s: {2, 5, 7}
t: {2, ’a’, ’b’, 7}
Union: {2, ’a’, 5, ’b’, 7}
Intersection: {2, 7}
Difference: {5}
Symmetric Difference: {’a’, 5, ’b’}

#Another way of creating a set that consists of the union of sets s and t is by using the method update. The difference is that s.update(t) does not return a value, but rather updates set s 
#.
s.update(t)
print(s)
{’b’, ’a’, 2, 5, 7}

Dictionaries
Dictionaries are used to create maps that associate values with keys. Dictionaries are
defined using curly brackets, just as sets. The only difference is that the list consists of
pairs of the form key:value .
name_age = {"Maria":24, "John":28, "Anna":35}
print(nameAge)
{’Maria’: 24, ’John’: 28, ’Anna’: 35}
The empty dictionary is denoted by {} . Do not confuse it with the empty set, which is
created using set() .
emptyDictionary = {}
print(emptyDictionary)
{}
Given a dictionary D, you can access the value associated to a key KEY by writing 
D[Key] .
nameAge = {"Maria":24, "John":28, "Anna":35}
print(nameAge["Maria"])
print(nameAge["John"])
print(nameAge["Anna"])
24
28
35
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Dictionaries 2
If you try to access the value of a key that does not exist, the interpreter will throw an
error. You can create a new pair KEY:VALUE by writing D[KEY] = VALUE . The same
operation can be used to change the value of key that is already present in the
dictionary.
nameAge = {"Maria":24, "John":28, "Anna":35}
print(nameAge)
#print(nameAge["Carlos"]) # Error message
nameAge["Carlos"] = 32
print(nameAge)
nameAge["Carlos"] = 47
print(nameAge)
{’Maria’: 24, ’John’: 28, ’Anna’: 35}
{’Maria’: 24, ’John’: 28, ’Anna’: 35, ’Carlos’: 32}
{’Maria’: 24, ’John’: 28, ’Anna’: 35, ’Carlos’: 47}
Use the construction x in D.keys() for testing whether a given key x is mapped to
some value in the dictionary.
nameAge = {"Maria":24, "John":28, "Anna":35}
print("Maria" in nameAge.keys())
print("Carlos" in nameAge)
True
False
To delete a pair KEY:Value from a dictionary, you can use either the del statement or the
pop method. 
nameAge = {"Maria":24, "John":28, "Anna":35}
print(nameAge)
del nameAge["Maria"]
print(nameAge)
value = nameAge.pop("John")
print(nameAge)
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Dictionaries 3
{’Maria’: 24, ’John’: 28, ’Anna’: 35}
{’John’: 28, ’Anna’: 35}
{’Anna’: 35}
You can iterate over the keys of a dictionary D using a for loop in a similar way to
iteration over lists. 
for x in D:
doSomething(x)
Note that the construction above iterates over keys. To iterate over values associated
with keys, then we iterate over the keys using a variable x and access the value
associated with a key using the index notation D[x] .
for x in D:
doSomething(D[x])
For instance, in the following example we show how to print the pairs of the form 
KEY:VALUE one per line.
nameAge = {’Maria’: 24, ’John’: 28, ’Anna’: 35, ’Carlos’: 47}
for x in nameAge:
print(x,end = ": ")
print(nameAge[x])
Maria: 24
John: 28
Anna: 35
Carlos: 47
Finally, the following example shows how to use dictionaries to store elements of a
custom class, and to retrieve such elements using one of the attributes as a key.
class Employee:
def __init__(self,id,name,age):
self.id = id
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
Dictionaries 4
self.name = name
self.age = age
def printEmployee(self):
print("("+self.name+","+str(self.age)+")")
company = {}
e = Employee("12393","Maria",29)
company[e.id] = e
e = Employee("19283","John",30)
company[e.id] = e
for x in company:
company[x].printEmployee()
(Maria,29)
(John,30)