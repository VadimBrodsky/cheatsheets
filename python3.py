# basic primitive types, all of these are immutable
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

# string escape characters \" \' \\ \n
message = "I'm in a bottle"         # double quote
message = 'I\'m in a bottle'        # single quote with escape
message = """I'm in a bottle"""     # multiline string

# formatted strings, expression that is evaluated at runtime
first, last = "John", "Snow"
full = f"{first} {last}"            # >>> 'John Snow

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

# numbers
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
import math
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
