import sys #PYTHON Get Started
import random #PYTHON Numbers

print("Hello, World!") #PYTHON HOME

print(sys.version) #PYTHON Get Started

if 5 > 2: #at least one space is required, 4 is the most commonly used. In the same block - the same number of spaces
    print("Five is greater than two!") #PYTHON Syntax

x = 5 #variables
y = "Hello, World!" #PYTHON Syntax

"""comments may be like this. it will be ignored""" #PYTHON Comments

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

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

#camel case: each word, except the first, starts with a capital letter (myVariableName = "John")
#pascal case: each word starts with a capital letter (MyVariableName = "John")
#snake case: each word is separated by an underscore character (my_variable_name = "John")

#Python allows to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Number of variables = number of values!

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python output:
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

"""
Will be error:
    x = 5
    y = "John"
    print(x + y)
"""

#the best way is to use commas:
x = 5
y = "John"
print(x, y)

#global variables:
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

#the variable created in the function is local, but we can use "global" keyword to create a global variable inside the function
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#we can change the global variable inside the function:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Data types:
t = "Hello World" #str
print(t)

t = 20 #int
print(t)

t = 20.5 #float
print(t)

t = 1j #complex
print(t)

t = ["apple", "banana", "cherry"] #list
print(t)

t = ("apple", "banana", "cherry") #tuple
print(t)

t = range(6) #range
print(t)

t = {"name" : "John", "age" : 36} #dict
print(t)

t = {"apple", "banana", "cherry"} #set
print(t)

t = frozenset({"apple", "banana", "cherry"}) #frozenset
print(t)

t = True #bool
print(t)

t = b"Hello" #bytes
print(t)

t = bytearray(5) #bytearray
print(t)

t = memoryview(bytes(5)) #memoryview
print(t)

t = None #NoneType
print(t)

#Setting the Specific Data Type:
g = str("Hello World")
g = int(20)
g = float(20.5)
g = complex(1j)
g = list(("apple", "banana", "cherry"))
g = tuple(("apple", "banana", "cherry"))
g = range(6)
g = dict(name="John", age=36)
g = set(("apple", "banana", "cherry"))
g = frozenset(("apple", "banana", "cherry"))
g = bool(5)
g = bytes(5)
g = bytearray(5)
g = memoryview(bytes(5))


#Python Numbers:
#int (integer) is a whole number, positive or negative, without decimals, of unlimited length:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float (floating point number) is a number, positive or negative, containing one or more decimals:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#float can also be scientific numbers with an "e" to indicate the power of 10:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
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
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#float:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#strings:
print("Hello")
print('Hello')

#Quotes Inside Quotes. They should not be the same as the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable:
a = "Hello"
print(a)

#Multiline Strings:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays:
a = "Hello, World!"
print(a[1])

#Looping Through a String:
for x in "banana":
    print(x)

#String Length:
a = "Hello, World!"
print(len(a))

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
b = "Hello, World!"
print(b[2:5])

#Slice From the Start:
b = "Hello, World!"
print(b[:5])

#Slice To the End:
b = "Hello, World!"
print(b[2:])

#Negative Indexing (starts the slice from the end of the string):
b = "Hello, World!"
print(b[-5:-2])


#Modify strings:
#Upper Case:
a = "Hello, World!"
print(a.upper())

#Lower Case:
a = "Hello, World!"
print(a.lower())

#Remove Whitespace (Whitespace is the space before and/or after the actual text).
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String (The replace() method replaces a string with another string):
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String (The split() method returns a list where the text between the specified separator becomes the list items).
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


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


#String Format.
"""
We cannot do this:
age = 36
txt = "My name is John, I am " + age
print(txt)
"""
#instead of this we can use f-strings or the format() method:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers. A placeholder can contain variables, operations, functions, and modifiers to format the value:
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)


#Escape Character.
"""
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""
#error:
#txt = "We are the so-called "Vikings" from the north."

#not an error:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Escape Characters:

#\' 	Single Quote 	
print(f"\'")
#\\ 	Backslash 
print(f"\\")	
#\n 	New Line
print(f"a-\n-b") 	
#\r 	Carriage Return 	
print("Hello-\r-World!")
#\t 	Tab 	
print("Hello-\t-World!")
#\b 	Backspace 	
print("Hello-\b-World!")
#\f 	Form Feed 	
print("Hello-\f-World!")
#\ooo 	Octal value (A backslash followed by three integers will result in a octal value)	
print("\"\110\145\154\154\157\" in a octal value")
#\xhh 	Hex value (A backslash followed by an 'x' and a hex number represents a hex value)
print("\"\x48\x65\x6c\x6c\x6f\" in a hex value")


#String Methods:
"""
capitalize() — Converts the first character to upper case
casefold() — Converts string into lower case
center() — Returns a centered string
count() — Returns the number of times a specified value occurs in a string
encode() — Returns an encoded version of the string
endswith() — Returns true if the string ends with the specified value
expandtabs() — Sets the tab size of the string
find() — Searches the string for a specified value and returns the position of where it was found
format() — Formats specified values in a string
format_map() — Formats specified values in a string
index()	— Searches the string for a specified value and returns the position of where it was found
isalnum() — Returns True if all characters in the string are alphanumeric
isalpha() — Returns True if all characters in the string are in the alphabet
isascii() — Returns True if all characters in the string are ascii characters
isdecimal()	— Returns True if all characters in the string are decimals
isdigit() — Returns True if all characters in the string are digits
isidentifier() — Returns True if the string is an identifier
islower() — Returns True if all characters in the string are lower case
isnumeric() — Returns True if all characters in the string are numeric
isprintable() — Returns True if all characters in the string are printable
isspace() — Returns True if all characters in the string are whitespaces
istitle() — Returns True if the string follows the rules of a title
isupper() — Returns True if all characters in the string are upper case
join() — Joins the elements of an iterable to the end of the string
ljust()	— Returns a left justified version of the string
lower()	— Converts a string into lower case
lstrip() — Returns a left trim version of the string
maketrans()	— Returns a translation table to be used in translations
partition()	— Returns a tuple where the string is parted into three parts
replace() — Returns a string where a specified value is replaced with a specified value
rfind()	— Searches the string for a specified value and returns the last position of where it was found
rindex() — Searches the string for a specified value and returns the last position of where it was found
rjust()	— Returns a right justified version of the string
rpartition() — Returns a tuple where the string is parted into three parts
rsplit() — Splits the string at the specified separator, and returns a list
rstrip() — Returns a right trim version of the string
split()	— Splits the string at the specified separator, and returns a list
splitlines() — Splits the string at line breaks and returns a list
startswith() — Returns true if the string starts with the specified value
strip() — Returns a trimmed version of the string
swapcase() — Swaps cases, lower case becomes upper case and vice versa
title()	— Converts the first character of each word to upper case
translate()	— Returns a translated string
upper()	— Converts a string into upper case
zfill() — Fills the string with a specified number of 0 values at the beginning
"""