import sys #PYTHON Get Started
import random #PYTHON Numbers

print("Hello, World!") #PYTHON HOME

print(sys.version) #PYTHON Get Started

if 5 > 2: #at least one space is required, 4 is the most commonly used. In the same block - the same number of spaces
    print("Five is greater than two!") #PYTHON Syntax

x1 = 5 #variables
y1 = "Hello, World!" #PYTHON Syntax

"""comments may be like this. it will be ignored""" #PYTHON Comments

x2 = 5
y2 = "John"
print(x2)
print(y2)

x3 = 4       # x3 is of type int
x3 = "Sally" # x3 is now of type str
print(x3)

x4 = str(3)    # x4 will be '3'
y4 = int(3)    # y4 will be 3
z4 = float(3)  # z4 will be 3.0

x5 = 5
y5 = "John"
print(type(x5))
print(type(y5))

x6 = "John"
# is the same as
x6 = 'John'

a = 4
A = "Sally" #this is a constant
#A will not overwrite a

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 
#legal: (a-A, 0-9 (not in start), _)
#variables are case-sensitive

"""
Illegal variable names:
    2myvar = "John"
    my-var = "John"
    my var = "John" 
"""

#camel case: each word, except the first, stars with a capital letter (myVariableName = "John")
#pascal case: each word stars with a capital letter (MyVariableName = "John")
#snake case: each word is separated by an underscore character (my_variable_name = "John")

#Python allows to assign values to multiple variables in one line:
x7, y7, z7 = "Orange", "Banana", "Cherry"
print(x7)
print(y7)
print(z7)
#Number of variables = number of values!

x8 = y8 = z8 = "Orange"
print(x8)
print(y8)
print(z8)

#Unpacking:
fruits = ["apple", "banana", "cherry"]
x9, y9, z9 = fruits
print(x9)
print(y9)
print(z9)

#Python output:
x10 = "Python is awesome"
print(x10)

x11 = "Python"
y11 = "is"
z11 = "awesome"
print(x11, y11, z11)

x12 = "Python "
y12 = "is "
z12 = "awesome"
print(x12 + y12 + z12)

x13 = 5
y13 = 10
print(x13 + y13)

"""
Will be error:
    x = 5
    y = "John"
    print(x + y)
"""

#the best way is t use commas:
x14 = 5
y14 = "John"
print(x14, y14)

#global variables:
x15 = "awesome"

def myfunc():
  x15 = "fantastic"
  print("Python is " + x15)

myfunc()

#the variable created in the function is local, but we can use "global" keyword to create a global variable inside the function
print("Python is " + x15)

def myfunc():
  global x16
  x16 = "fantastic"

myfunc()

print("Python is " + x16)

#we can change the global variable inside the function:
x17 = "awesome"

def myfunc():
  global x17
  x17 = "fantastic"

myfunc()

print("Python is " + x17)


#Data types:
t1 = "Hello World" #str
print(t1)

t2 = 20 #int
print(t2)

t3 = 20.5 #float
print(t3)

t4 = 1j #complex
print(t4)

t5 = ["apple", "banana", "cherry"] #list
print(t5)

t6 = ("apple", "banana", "cherry") #tuple
print(t6)

t7 = range(6) #range
print(t7)

t8 = {"name" : "John", "age" : 36} #dict
print(t8)

t9 = {"apple", "banana", "cherry"} #set
print(t9)

t10 = frozenset({"apple", "banana", "cherry"}) #frozenset
print(t10)

t11 = True #bool
print(t11)

t12 = b"Hello" #bytes
print(t12)

t13 = bytearray(5) #bytearray
print(t13)

t14 = memoryview(bytes(5)) #memoryview
print(t14)

t15 = None #NoneType
print(t15)

#Setting the Specific Data Type:
g1 = str("Hello World")
g2 = int(20)
g3 = float(20.5)
g4 = complex(1j)
g5 = list(("apple", "banana", "cherry"))
g6 = tuple(("apple", "banana", "cherry"))
g7 = range(6)
g8 = dict(name="John", age=36)
g9 = set(("apple", "banana", "cherry"))
g10 = frozenset(("apple", "banana", "cherry"))
g11 = bool(5)
g12 = bytes(5)
g13 = bytearray(5)
g14 = memoryview(bytes(5))


#Python Numbers:
#int (integer) is a whole number, positive or negative, without decimals, of unlimited length:
x18 = 1
y18 = 35656222554887711
z18 = -3255522

print(type(x18))
print(type(y18))
print(type(z18))

#float (floating point number) is a number, positive or negative, containing one or more decimals:
x19 = 1.10
y19 = 1.0
z19 = -35.59

print(type(x19))
print(type(y19))
print(type(z19))

#float can also be scientific numbers with an "e" to indicate the power of 10:
x20 = 35e3
y20 = 12E4
z20 = -87.7e100

print(type(x20))
print(type(y20))
print(type(z20))

#complex numbers are written with a "j" as the imaginary part:
x21 = 3+5j
y21 = 5j
z21 = -5j

print(type(x21))
print(type(y21))
print(type(z21))

#Type Conversion:
x22 = 1    # int
y22 = 2.8  # float
z22 = 1j   # complex

#convert from int to float:
a2 = float(x22)

#convert from float to int:
b2 = int(y22)

#convert from int to complex:
c2 = complex(x22)

print(a2)
print(b2)
print(c2)

print(type(a2))
print(type(b2))
print(type(c2))
#it cannot convert complex numbers into another number type

#Random Number:
print(random.randrange(1, 10))


#Python Casting:
"""
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""

#int:
x23 = int(1)   # x23 will be 1
y23 = int(2.8) # y23 will be 2
z23 = int("3") # z23 will be 3

#float:
x24 = float(1)     # x24 will be 1.0
y24 = float(2.8)   # y24 will be 2.8
z24 = float("3")   # z24 will be 3.0
w24 = float("4.2") # w24 will be 4.2

#strings:
x25 = str("s1") # x25 will be 's1'
y25 = str(2)    # y25 will be '2'
z25 = str(3.0)  # z25 will be '3.0'


#strings:
print("Hello")
print('Hello')

#Quotes Inside Quotes. They should not be the same as the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable:
a3 = "Hello"
print(a3)

#Multiline Strings:
a4 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a4)
#or:
a5 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a5)

#Strings are Arrays:
a6 = "Hello, World!"
print(a6[1])

#Looping Through a String:
for x in "banana":
    print(x)

#String Length:
a7 = "Hello, World!"
print(len(a7))

#Check String:
txt = "The best things in life are free!"
print("free" in txt) #"in" checks
#or:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT:
txt = "The best things in life are free!"
print("expensive" not in txt) #"not in" checks
#or:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Slicing:
b3 = "Hello, World!"
print(b3[2:5])

#Slice From the Start:
b4 = "Hello, World!"
print(b4[:5])

#Slice To the End:
b5 = "Hello, World!"
print(b5[2:])

#Negative Indexing (starts the slice from the end of the string):
b6 = "Hello, World!"
print(b6[-5:-2])


#Modify strings:
#Upper Case:
a8 = "Hello, World!"
print(a8.upper())

#Lower Case:
a9 = "Hello, World!"
print(a9.lower())

#Remove Whitespace (Whitespace is the space before and/or after the actual text).
#The strip() method removes any whitespace from the beginning or the end:
a10 = " Hello, World! "
print(a10.strip()) # returns "Hello, World!"

#Replace String (The replace() method replaces a string with another string):
a11 = "Hello, World!"
print(a11.replace("H", "J"))

#Split String (The split() method returns a list where the text between the specified separator becomes the list items).
#The split() method splits the string into substrings if it finds instances of the separator:
a12 = "Hello, World!"
print(a12.split(",")) # returns ['Hello', ' World!']


#String Concatenation.
#To concatenate, or combine, two strings we can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)