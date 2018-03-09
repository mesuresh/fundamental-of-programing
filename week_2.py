# week 2

# Today we will learn the following things
# Comments, Operators, Keywords, Variables (Global and Local), Constant, Strings, and Numbers, Type Casting

#--------------- 1. Comments -----------------------------
# Here we will learn comments 
# This is one line comments
'''
This is multiple line comments.
Here you can type any number of lines
The comments ends here.
'''


#--------------- 2. Operators -----------------------------
'''
Operators are special symbols in Python that carry out arithmetic or logical computation. 
The value that the operator operates on is called the operand.
'''
# Refer this this url: https://www.programiz.com/python-programming/operators
# Arithmetic operators, Comparison operators, Logical operators, 
'''
Exercise: refer: https://www.programiz.com/python-programming/operators
1. run code of Arithmetic operators
2. run code of Comparison operators
3. run code of Logical operators
'''

#--------------- 3. Keywords -----------------------------
# Keywords are the reserved words in Python. 
# We cannot use a keyword as variable name, function name or any other identifier.
'''
False    class    finally    is    return
None    continue    for    lambda    try
True    def    from    nonlocal    while
and    del    global    not    with
as    elif    if    or    yield
assert    else    import    pass     
break    except    in    raise     
'''
# importing keywords
# import keyword
# print(keyword.kwlist)
#--------------- 4. Variables and data types -----------------------------
'''
Variables are nothing but reserved memory locations to store values. 
This means that when you create a variable you reserve some space in memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. 
Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

Assigning Values to Variables
Python variables do not need explicit declaration to reserve memory space. 
The declaration happens automatically when you assign a value to a variable. 
The equal sign (=) is used to assign values to variables.
'''
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)
# -----------> data types
# integer, string, float, tuple, list, dict, datetime

# print(type("Hello world")) # string data type
# print(type(1)) # integer
# print(type(1.2)) # float

a = b = c = 1 #Multiple assignments
print(a,b,c)
a,b,c = 1,2,"john" # another way for Multiple assignments
print(a,b,c)

'''
Exercise:
1. Find the data type of [1,2,3,4]
2. Find me data type of {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
'''
#--------------- 5. Strings -----------------------------
# String are the sequence of characters
# fruit = 'Banana'  # "" or '' are equivalent
# You can assign first character to another variables as:
# letter = fruit[0]
# print(fruit)
# print(letter)
# print(len(fruit))
# print(fruit[-1]) # last character
# print(fruit[-2]) # second last character
# print(fruit[0:2]) # first two characters
# print(fruit[3:6]) # first two characters
# print(fruit[:-2]) # exclude last two digits
# print(fruit[2:]) # exclude first two digits
# # A bit different style
# print("Length of banana is {}".format(len(fruit))) # Printing length of banana

'''
Exercise:
1. Find me last four digit of a word 'Programming'
2. Find me length of sequence 'Hello world'
3. Print me the string by excluding first two and last two characters of string 'joker' using len funtion
'''
# print("First Character of '{}' is '{}' and length is {}".format(fruit,letter,len(fruit)))

#--------------- 5. Numbers -----------------------------
# int, float, complex
# import math
# balance = 2005.10
# x=2
# print(abs(balance)) # absolute value: positive number
# print(math.ceil(balance)) # above number # similar for lower value use floor
# print(math.exp(x))

# other functions : log, log10, max(x1,x2,x3), min(....), math.modf(12/5) for remainder, round(x [,n]), sqrt(x), tan, cosine, pi, e, 
# look here: https://www.tutorialspoint.com/python/python_numbers.htm
'''
Exercise:
1. Find me the floor of 12.05
2. Find the the maximum reminder of 12/5, 14/4, 20/17
3. Print me the log of 12pi 
4. Find me exponetial of 5
5. Find the pi value
'''

#--------------- 6. Type casting -----------------------------
# type casting is conversion of one data type to another data type.

print(int('1') + int('2')) # adding two integer after type cast string to integer
print(str(1)+str(2)) #string addition is concatenation
str1 = "hi1fr"
str2 = 'hi2fr'
# Exercise: extract integer number from both string str1 and str 2 and add it



