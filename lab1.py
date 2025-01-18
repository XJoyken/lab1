import sys #PYTHON Get Started

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
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


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