# ============================================================
# PYTHON COLLECTIONS: FUNCTIONS
# ============================================================
# In this file, we will learn:
# 1. Why we use functions
# 2. Defining and calling a function
# 3. Parameters
# 4. return vs print
# 5. Default arguments
# 6. Lambda functions
# 7. Your turn: two small interactive tasks
# ============================================================


# ------------------------------------------------------------
# 1. WHY FUNCTIONS?
# ------------------------------------------------------------
# A function is a reusable block of code with a name.
# Write it once, use it as many times as you like.


# ------------------------------------------------------------
# 2. DEFINING AND CALLING A FUNCTION
# ------------------------------------------------------------
# Use def to define a function. The code inside must be indented.
# Nothing runs until you CALL the function.

def say_hello():
    print("Hello from a function!")


say_hello()
say_hello()


# ------------------------------------------------------------
# 3. PARAMETERS
# ------------------------------------------------------------
# Parameters let us pass values into a function.

def greet(name):
    print("Hello,", name + "!")


print("\n--- Parameters ---")

greet("Aarav")
greet("Diya")


# ------------------------------------------------------------
# 4. return VS print
# ------------------------------------------------------------
# print() only SHOWS a value on the screen.
# return SENDS a value back so the rest of the program can use it.

def add(a, b):
    return a + b


print("\n--- return ---")

result = add(3, 4)
print("3 + 4 =", result)
print("Double of the result:", result * 2)

# A common mistake: a function that prints but does not return.
def add_wrong(a, b):
    print(a + b)


value = add_wrong(3, 4)
print("value is", value)      # None, because nothing was returned


# ------------------------------------------------------------
# 5. DEFAULT ARGUMENTS
# ------------------------------------------------------------
# A parameter can have a default value.
# If the caller does not give one, the default is used.

def power(base, exponent=2):
    return base ** exponent


print("\n--- Default Arguments ---")

print("power(5):", power(5))          # uses exponent = 2
print("power(5, 3):", power(5, 3))    # overrides the default


# ------------------------------------------------------------
# 6. LAMBDA FUNCTIONS
# ------------------------------------------------------------
# A lambda is a tiny one-line function with no name.

def square(x):
    return x * x


square_lambda = lambda x: x * x

print("\n--- Lambda ---")

print("square(4):", square(4))
print("square_lambda(4):", square_lambda(4))

# Lambdas are handy as a sorting rule.
names = ["Ada Lovelace", "Grace Hopper", "Alan Turing"]
print("Sorted by name length:", sorted(names, key=lambda n: len(n)))


# ------------------------------------------------------------
# YOUR TURN (EASY): AREA OF A RECTANGLE
# ------------------------------------------------------------
# Finish the function so it RETURNS the area.
# Do not print inside the function.
#
# Example: length 5 and breadth 3 should print Area: 15.0

print("\n--- Your Turn: Area of a Rectangle ---")


def area_rectangle(length, breadth):
    # TODO: return the area of the rectangle
    pass


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

print("Area:", area_rectangle(length, breadth))


# ------------------------------------------------------------
# YOUR TURN (MEDIUM): PASS OR FAIL
# ------------------------------------------------------------
# Finish grade(marks, pass_mark=40) so it returns "Pass" if
# marks are at least pass_mark, and "Fail" otherwise.
#
# Example:
#   grade(55)      ->  Pass    (default pass mark is 40)
#   grade(55, 60)  ->  Fail    (custom pass mark of 60)

print("\n--- Your Turn: Pass or Fail ---")


def grade(marks, pass_mark=40):
    # TODO: return "Pass" or "Fail"
    pass


marks = float(input("Enter your marks: "))
print("With the default pass mark:", grade(marks))

custom = float(input("Enter a custom pass mark: "))
print("With your pass mark:", grade(marks, custom))


# ------------------------------------------------------------
# BONUS CHALLENGE
# ------------------------------------------------------------
# 1. Write is_even(n) that returns True or False.
# 2. Write a lambda that cubes a number.
# 3. Write a function that takes a list and returns its average.
# ============================================================
