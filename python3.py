# Variables
number_of_snakes = 3                # int
rating = 4.99                       # float
is_published = True                 # bool
live_changes = False                # bool
famous_words = "Hello World"        # str

# multiple initialization
x, y = 1, 2
x = y = 1

# types and annotations
type(number_of_snakes) # >>> <class 'int'>
age: int = 30          # mypy linter would catch incorrect type assignments
