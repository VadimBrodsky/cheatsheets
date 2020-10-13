# Modules
# import modules at the top
###############################################################################
import math


# Basic Types
# basic primitive types, all of these are immutable
###############################################################################
number_of_snakes = 3                # int
rating = 4.99                       # float
is_published = True                 # bool
live_changes = False                # bool
famous_words = "Hello World"        # str


# a constant by convention only
PI = 3.14


# id is used to print the memory address
id(number_of_snakes)       # >>> 10914560
id(number_of_snakes + 1)   # >>> 10914592


# multiple initialization
x, y = 1, 2
x = y = 1


# types and annotations
type(number_of_snakes)  # >>> <class 'int'>
age: int = 30           # mypy linter would catch incorrect type assignments


# length of things
len(famous_words)       # >>> 11


# substring acccess
famous_words[0]         # >>> 'H'
famous_words[-1]        # >>> 'd'
famous_words[0:3]       # >>> 'Hel'
famous_words[:3]        # >>> 'Hel'
famous_words[0:]        # >>> 'Hello  World'
famous_words[:]         # >>> 'Hello  World'


# Strings
###############################################################################


# string escape characters \" \' \\ \n
message = "I'm in a bottle"         # double quote
message = 'I\'m in a bottle'        # single quote with escape
message = """I'm in a bottle"""     # multiline string


# formatted strings, expression that is evaluated at runtime
first, last = "John", "Snow"
full = f"{first} {last}"            # >>> 'John Snow'


# sting methods
famous_words.upper()                # >>> 'HELLO WORLD'
famous_words.lower()                # >>> 'hello world'
famous_words.title()                # >>> 'Hello World'


# white space
"   blanks ".strip()                # >>> 'blanks'
"     left".lstrip()                # >>> 'left'
"right    ".rstrip()                # >>> 'right'


# finding substring
famous_words.find("Wor")                # >>> 6
famous_words.replace("Hello", "Bye")    # >>> 'Bye World'
"World" in famous_words                 # >>> True
"World" not in famous_words             # >>> False


# Numbers
###############################################################################


decimal_number = 10
binary_number = 0b10               # bin(binary_number) >>> '0b10'
hexadecimal_number = 0x12c         # hex(hexadecimal_number) >>> '0x12c'
complex_number = 2j                # complex(complex_number) >>> '2j'


# arithmetic operations
# all of these can be augmented for assignment: 10 += 3
10 + 3                             # sum
10 - 3                             # difference
10 * 3                             # product
10 / 3                             # quotient, decimal
10 // 3                            # quotient, integer
10 % 3                             # modulo, remainder
10 ** 3                            # exponent


round(PI)                          # 3
abs(-PI)                           # 3.14


# math module, for more math functions
math.floor(PI)                     # 3

# get input from the command line
z = input("x: ")


# type conversions, python does not do anything implicitly
# falsey values: "", 0, [], None
# everything else is Truthy


# assuming z is '1'
int(z)                            # 1
float(z)                          # 1.0
bool(z)                           # True
str(z)                            # '1'


# Conditionals
# if else statemnts using boolean operators: == != >= <= > <
###############################################################################


age = 22
if age >= 18:
    # block defined using white space
    print('Adult')
# else if in python is elif
elif age >= 13:
    print('Teenager')
else:
    print('Child')


if True:
    # cannot have an empty block
    # use pass keyword instead
    pass


# logical operators: and, or, not
empty_string = ''
if not empty_string:
    print('string is empty')


# and logic operator
if age >= 18 and age < 65:
    print('Eligible')


# can use a chaining comparison operator
if 18 <= age < 65:
    print('Eligible')


# ternary operators, use if and else inline
message = 'Eligibile' if age >= 18 else 'Not Eligible'


# Loops
# for and while, loops iterate over any iterable object
###############################################################################


# iterate over string characters
for j in 'Python':
    print(x)


# iterate over list items
for j in ['a', 'b', 'c']:
    print(x)


# iterate over range of numbers using range function
for x in range(5):
    print(x)


# range can take additional arguments: range(start, stop, step)
for x in range(0, 10, 2):
    print(x)


# for else loop, if the loop didn not break
names = ['John', 'Ned']
for name in names:
    if name.startswith('J'):
        print('Found')
        # break from the loop
        break
else:  # if the loop did not break
    print('Not found')


# while, while else loops:
guess, answer = 0, 5
while answer != guess:
    guess = int(input('Make a guess: '))
else:  # if the while loop completed without a break
    pass


# Functions
# return None if no return specified
# can return multiple items by using a tuple (read only list)
###############################################################################


def incement(number, by):
    return number + by


incement(2, 3)                         # >>> 5


def incement_tuple(number, by):
    return (number, number + by)


incement_tuple(2, 3)                   # >>> (2, 5)


def increment_with_default_value(number, by=1):
    return number + by


increment_with_default_value(2)        # >>> 5

# pass a keyword argument
increment_with_default_value(2, by=4)  # >>> 6


def increment_with_types(number: int, by: int = 1) -> tuple:
    return (number, number + by)


increment_with_types(2, 4 )            # >>> 6
