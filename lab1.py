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