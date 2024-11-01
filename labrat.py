#variable is used for storing data, strings are stored in double quotes
name = input("What is your name?")
date = input("Input your preferred Date")
time = input ("Input your preferred Time")
feedback = "Dear "+ name +" your appointment is scheduled for, "+ date +" at "+ time +". Do well to be at the premises 30 minutes fbefore your scheduled time"
#print function is used to display text in the screen 
print(feedback)


File Basics 1
File Basics
File Modes
In Python, files are opened by calling the function open(filename,mode) . Here, filename is
the name of the file to be open (a string), while mode is a parameter that specifies the
mode in which the file will be open, that is to say, for reading, writing, text mode, binary
mode, etc. This function returns a file object that is used as an interface between the
program and the open file. The following options can be used to specify the mode. 
1. Read Mode ( "r" ): opens a file for reading. If the file does not exists it casts an error
message.
2. Write Mode ( "w" ): opens a file for writing. If the file does not exist, it is created. If
the file exists, it is truncated (content erased) and overwritten by the new
information written to the file.
3. Append Mode ( "a" ): opens a file for appending. If the file does not exist, it is
created. If the file exists, the new information is written at the end of the file.
4. Read and Write mode ( "r+" ): opens a file for reading and writing. If the file does not
exist, an error message is cast. The content of the file is preserved. New content
written at a given position in the file replaces the old content up to the length of the
new content.
5. Write and Read Mode ("w+") : opens a file for reading and writing. If the file does
not exist, it is created. If the file exists, it is truncated (content erased).
6. Append and Read Mode ( "a+" ): opens a file for reading and appending. If the file
does not exist, it is created. If the file exists, the new information is written at the
end of the file.
7. Exclusive creation Mode ("x") : creates a new file if it does not exist. Casts an error
if the file already exists.
8. Text modes ( "rt" , "wt" , "at" , "r+t" , "w+t" , "xt" ): These are precisely the
modes described above. When the letter t is omitted, the default is text mode.
9. Binary modes ( "rb" , "wb" , "ab" , "r+b" , "w+b" , "xb" ): All previously discussed
modes are concern text files. Binary modes are used to create/read/write binary
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 2
files, such as images.
Getting the Content of a Text File as a String
The most elementary way of opening a file for reading is to use the instruction 
file = open(filename,"r") . Here, the parameter filename is the name of the file, while
the option "r" is an option that specifies that the file is being opened for reading.
Finally, file is a variable that stores a file object that can be used to access the file we
are opening. 
# Opening a file with file = open(filename,r)
filename = "example.txt"
file = open(filename, "r") # Opening the file
content = file.read() # Reading the file content
print(content)
file.close() # Closing the file explicitly
The instruction content = file.read() reads the whole content of the file and stores it in
variable content . Note that when reading files in this way, the variable content is a string
containing all characters of the file, including whitespaces ( ) and new line characters
( \n ). For demonstration purposes, we are using the instruction print(content) to print
the content of the file in the terminal. For example, assume that our file example.txt
contains the following list of pets: 
cat
dog
guinea pig
hamster
Then this list will be printed in the terminal. Please note that, the string content contains
all white spaces and new line characters of the text file, that is, content =
"cat\ndog\nguinea pig\nhamster" . To see this, you can use the instruction 
print(repr(content)) instead of print(content) . 
Finally, the instruction file.close() explicitly tells python to close the file. It is important
to note that when opening a file using file = open(filename, "r") , the file remains open
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 3
until we explicitly close it by calling file.close() . If we forget to close the file, it will
remain open until it is closed by the Python interpreter. In some cases, this may lead to
issues such as data loss, file corruption, etc. Therefore, it is recommended to always
close a file explicitly once it no longer used in the code. 
A Safer Option: The with Statement
A safer alternative for opening files is using the construction with open(filename, "r") as
file as exemplified below. 
# Opening and reading the file content within a 'with' block
filename = "example.txt"
with open(filename, "r") as file:
 content = file.read()
 print(content)
# The file is automatically closed upon exiting the 'with' block
In this case, the file is automatically closed when the with block is exited, even if an
exception occurs within the block. This makes the code cleaner since with takes care
of closing the file for us. The obtained result is the same as in the previous case. 
cat
dog
guinea pig
hamster
In most cases, due to better readability and code management, the construction above
is preferrable over the option of opening and closing a file explicitly, although the later
may still be useful in situations where one wishes to keep a file open over an extended
period, or across multiple scopes in the code.
Reading a Text File Partially
By default, when called without a parameter, the method read() will read the whole file
as a string. To read only the n first characters of the file (counting with whitespaces and
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 4
new line characters), one may pass the number n as a parameter to the read method,
as exemplified below. 
filename = "example.txt
n = 10 # number of characters to be read. 
with open(filename, "r") as file:
 partial_content = file.read(n)
 print(partial_content)
For example, when setting n=10 in our previous example, the in our example, where the
file has a list of pets, the program will print the following information in the terminal. 
cat
dog
gu
Iterating Through the Lines of a Text File
Sometimes, we want to iterate through individual lines of a file. There are three main
ways of doing that. The first two use a for loop read the file line by line. The third
method reads the whole file as a list of lines. 
A) Using a for loop directly on the file object:
Here, the file object itself is iterable, and it yields one line at a time when iterated over
with a for loop, as exemplified below. 
filename = "example.txt"
with open(filename, "r") as file:
 for line in file:
 print(line.strip()) # strip() is used to remove leading and trailing whitespaces
including newline characters
Here, the variable line is of type str (or more precisely, <class 'str'> ). Note that
Python knows that a line has been read because either it has reached a new line
character, or because it has reached the end of file. The strip() method is used to
remove the new line character, as well as any trailing whitespaces. 
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 5
cat
dog
guinea pig
hamster
B) Reading line by line with readline(). 
A very similar method uses the readline() .
with open("example.txt", "r") as file:
 line = file.readline()
 while line:
 print(line.strip())
 line = file.readline()
As in the previous example, here, line is also a variable of type str . In this particular
example, python keeps reading a line until the file has arrived to an end. In this case, 
line will be the empty string "" , which will cause the loop to halt, since in a Boolean
context, the empty string is equivalent to False . 
cat
dog
guinea pig
hamster
The advantage of the method readline() is that it gives us more control over when a
line should be read. For instance, we could use loops with more complex stopping
conditions, or choose to read individual lines within distinct blocks of code. 
Using readlines() method:
Finally, we may also consider reading the whole file at once as a list of lines using the
method readlines() (note the plural). 
filename = "example.txt"
with open(filename, "r") as file:
 lines = file.readlines()
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 6
for line in lines:
 print(line.strip()) # strip() is used to remove leading and trailing whitespaces incl
uding newline characters
Note that the variable lines has the type of a list. The advantage of this method is that
it gives us more flexibility to manipulate the lines of the file, since once they are read,
they are stored in a list. We may then process the list using other types of iteration, such
as iteration over indices, etc. 
It is worth noting that while readlines() method can be convenient, we need to be
cautious when using it to read very large files, since in this case, the content of the
whole file will be present in the memory at once. If memory consumption is a concern,
the previous method, where each line is read individually is preferrable. 
Writing on Files
Next, we discuss some common methods for writing information on text files.
Creating a new file and writing a string to it. 
As we have seen above when reading a text file, we may store its content in a variable 
content . We can proceed in the opposite direction and write the content of a string into
a file. The only difference is that we will now use the option 'w' to specify that the file is
being open in write mode. 
with open("exampleWrite.txt", "w") as file:
content = "cat\ndog\nguinea pig\nhamster"
file.write(content)
As a result, we get the following file: 
cat
dog
guinea pig
hamster
We may also use several write operations to write in a file, while the file is open. For
example the same result would have been obtained if we had used the the following two
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 7
write operations. 
with open("exampleWrite.txt", "w") as file:
content1 = "cat\ndog\n"
content2 = "guinea pig\nhamster"
file.write(content1)
file.write(content2)
Copying one file into another 
We can open two files at the same time using the with statement in Python. It allows
you to open multiple files in a clean and efficient manner, ensuring that all files are
properly closed after their intended operations are performed. 
# Open two files simultaneously
with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
 # Read content from the first file
 content = file1.read()
 # Write content to the second file
 file2.write(content)
# Both files will be automatically closed when exiting the with block
In this example, the instruction with open("file1.txt", "r") as file1 opens "file1.txt" in
read mode and assigns the file object to file1 , while open("file2.txt", "w") as file2
opens "file2.txt" in write mode and assigns the file object to file2 . The instruction 
content = file1.read() reads the entire content of 'file1.txt' , and stores it into variable 
content , while the instruction file2.write(content) writes the string stored in content into
the file 'file2.txt' . Finally, both files are automatically closed upon exiting the with
block.
Saving the User Input in a Text File 
The following program asks the user to enter three names, and stores these names in a
file called "testFile.txt". One name per line.
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 8
print("\nCreating file:")
file = open("testFile.txt", "wt")
for x in range(3):
 name = input("Enter a Name: ")
 #important: \n creates a new line for each answer
 file.write(name + "\n")
file.close()
Creating file:
Enter a Name: Maria
Enter a Name: John
Enter a Name: Ana
Saving a List in a Text File
Using a for loop, we may copy the content of a list to a file. 
fruits = ["Apple","Banana","Orange","Strawberry"]
with open("fruits.txt", "w") as file:
for fruit in fruits:
file.write(fruit + "\n")
The content of the resulting file, “fruits.txt” is the following. 
Apple
Banana
Orange
Strawberry
Please note that the write() method does not add a newline character at the end of the
line automatically. Therefore, if we want each entry of the list to be printed in a distinct
line, we need to add newline characters explicitly. 
Another option is to use the writelines(lines) method. This method takes as parameter
a list of elements and writes all elements of the list in the file. As in the previous case,
the method does not add a newline character at the end of each item automatically. So
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 9
if we want each entry to be in an individual line, each such entry must end with a
newline character \n . 
fruits = ["Apple\n","Banana\n","Orange\n","Strawberry\n"]
with open("fruits.txt", "w") as file:
for fruit in fruits:
file.write(fruit)
Apple
Banana
Orange
Strawberry
Saving a Dictionary in a Text File
Using a for loop we can also record the entries of a dictionary into a file 
name_number = {"Maria":35,"John":20,"Alice":32,"Carlos":25}
with open("name_number.txt", "w") as file:
for key in name_number:
file.write(key + ":" + str(name_number[key]) + "\n")
As a result, the file named “name_number.txt” contains the following lines. 
Maria:35
John:20
Alice:32
Carlos:25
Saving Synthetic Data in a Text File
One can also use files to save synthetic data, generated by computations performed
during the program. As a simple example of this case, we implement below a simple
program that writes a number and its square in a file. It is worth noting that the string to
be written in a file may be an f-string, which allows a better control in terms of
formatting. 
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 10
n = int(input("Number? "))
with open("functionTable.txt", "w") as file:
for x in range(1,n+1):
file.write(f"{x} squared is equal to {x**2}.\n")
1 squared is equal to 1.
2 squared is equal to 4.
3 squared is equal to 9.
4 squared is equal to 16.
5 squared is equal to 25.
Appending to a File. 
In the previous examples we opened files for writing using the option "w" . In this case,
if there is already a file with the same name as the file we are trying to open, then the
previously existing file will be truncated (that is, its original content will be erased) and
the file will be filled by the new content written to the file after the opening instruction. In
some cases, it may be more appropriate to open a file with the goal of appending
information, that is writing new information at the end of the file, without deleting the
previous text. For instance, this may be useful if we are using a file as a way of logging
information. To open a file for appending we use the option "a" . It is worth noting that if
a file with same name as the one we are trying to open does not yet exist, such file will
be created. The following program appends the sentence "Appending a Line." to the end
of a file. 
filename = "exampleAppend.txt"
with open(filename, 'a') as file:
 file.write("\nAppending a Line.")
For example, suppose that the file “exampleAppend.txt” has the following content. 
Line One 
Line Two
Line Three
Then, after executing our program, the resulting file becomes: 
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 11
Line One
Line Two
Line Three
Appending a Line.
Example: First Line of Text where a Word
Occurs
The following program takes as input a string filename and a string word , and returns
the first line of text where the word occurs. If the file does not exist it returns a message
saying that the file does not exist. If the file exits but the word is not in the file, then it
returns a message saying that the word does not exist in the file. 
def line_with_word(filename, word):
 if not os.path.exists(filename):
 return f"File '{filename}' does not exist." 
 
 with open(filename, 'r') as file:
 for line in file:
 if word in line:
 return line
 return f"Word '{word}' does not exit in file '{filename}'."
# We need to import the module 'os' to check if the file exists
import os
if __name__ == "__main__": 
 filename = "example.txt"
 word = "hello"
 print(line_with_word(filename, word))
Number of the First Line of Text Where a
Word Occurs
The next code is a variation of the previous one where instead of returning the first line
of text where a given word occur, it returns just the line number. If the word is not in the
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only
File Basics 12
file, the function number_line_with_word returns 0 , and if the file does not exist, the
function returns -1 . 
# obs: When talking about files, the first line is referred to line 1, not line 0
def number_line_with_word(filename, word):
 if not os.path.exists(filename):
 return -1
 
 with open(filename, 'r') as file:
 line_number = 1
 for line in file:
 if word in line:
 return line_number
 line_number += 1
 return 0
# We need to import the module 'os' to check if the file exists
import os
if __name__ == "__main__": 
 filename = "example.txt"
 word = "hello"
 result = number_line_with_word(filename, word)
 if result > 0:
 print(f"Word '{word}' found on line {result} of file '{filename}'.")
 elif result == 0:
 print(f"Word '{word}' not found in file '{filename}'.")
 else: # result == -1
 print(f"File '{filename}' does not exist.")
Copyright: Mateus de Oliveira Oliveira - September 2023 - For personal use only