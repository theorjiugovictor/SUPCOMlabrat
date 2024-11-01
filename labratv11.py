22
I N H E R I TA N C E
Inheritance is a feature of object oriented programming
that allows one to define classes that inherit attributes and
methods from another class. If class A inherits attributes
and methods from class B, then we say that A is a class
derived from B (or a child of B). Alternatively, one may say
that B is a base class, or that B is the parent of A.
The concept of inheritance is better illustrated through an
example. Consider for instance, the class Furniture whose
instances are meant to specify the dimensions of furnitures.
More specifically, this class has attributes height, width and
depth, and a method called printFurniture that will print
these dimensions.
class Furniture:
def __init__(self,height,width,depth):
self.height = height
self.width = width
self.depth = depth
def printFurniture(self):
print("Printing Furniture:")
print("Height:",self.height)
print("Width:",self.width)
print("Depth:",self.depth)
print()
f = Furniture(2,3,3)
f.printFurniture()
67
68 inheritance
Printing Furniture:
Height: 2
Width: 3
Depth: 3
Now, we will define a class called Sofa which should not
only have all attributes and methods of a furniture, but also
an attribute nSeats specifying the number of seats. Note that
in the initialization function of the class Sofa, we first call
the initialization function for the class Furniture, and then
initialize the attribute nSeats, which is peculiar to sofas.
class Sofa(Furniture):
def __init__(self,height,width,depth,nSeats):
Furniture.__init__(self,height,width,depth)
self.nSeats = nSeats
def printFurniture(self):
print("Printing Sofa:")
print("Height:",self.height)
print("Width:",self.width)
print("Depth:",self.depth)
print("NSeats:",self.nSeats)
print()
s = Sofa(1,2,1,4)
s.printFurniture()
Printing Sofa:
Height: 1
Width: 2
Depth: 1
NSeats: 4
Next, we will define a class called Table which should
not only have all attributes and methods of a furniture, but
also an attribute shape specifying the shape of the table (say,
"round" or "square"). Note that in the initialization function
of the class Table, we first call the initialization function
for the class Furniture, and then we initialize the attribute
shape, which is specific for tables.
inheritance 69
class Table(Furniture):
def __init__(self,height,width,depth,shape):
Furniture.__init__(self,height,width,depth)
self.shape = shape # round or square
def printFurniture(self):
print("Printing Table:")
print("Height:",self.height)
print("Width:",self.width)
print("Depth:",self.depth)
print("Shape:",self.shape)
print()
t = Table(1,1,2,"round")
t.printFurniture()
Printing Table:
Height: 1
Width: 1
Depth: 2
Shape: round
The next piece of code shows how one can use the variable
and method to deal with objects with distinct behaviors.
More specifically, we first add objects of type Sofa and
objects of type Table to a list called store. Then we iterate
through this list using a variable x and print each item by
calling the method x.printFurniture(). Note that, this
method will behave differently depending on whether the
current object referenced by x is of type Sofa or of type
Table.
store = []
store.append(Sofa(1,2,1,4))
store.append(Table(1,2,1,"round"))
store.append(Sofa(1,2,2.5,5))
store.append(Table(1,2,2,"square"))
for x in store:
x.printFurniture()
70 inheritance
Printing Sofa:
Height: 1
Width: 2
Depth: 1
NSeats: 4
Printing Table:
Height: 1
Width: 2
Depth: 1
Shape: round
Printing Sofa:
Height: 1
Width: 2
Depth: 2.5
NSeats: 5
Printing Table:
Height: 1
Width: 2
Depth: 2
Shape: square