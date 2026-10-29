# ============================================================
# PYTHON COLLECTIONS: LISTS AND TUPLES
# ============================================================
# In this file, we will learn:
# 1. Creating lists
# 2. Accessing items using indexing
# 3. Changing a list (append, remove, sort)
# 4. Looping through a list
# 5. Tuples and why they cannot be changed
# 6. Your turn: a small interactive task
# ============================================================


# ------------------------------------------------------------
# 1. CREATING LISTS
# ------------------------------------------------------------
# A list stores many values in one variable.
# Lists use square brackets and keep their items in order.

subjects = ["Python", "C++", "Mathematics", "OS"]

print("Subjects:", subjects)
print("Number of subjects:", len(subjects))


# ------------------------------------------------------------
# 2. ACCESSING ITEMS
# ------------------------------------------------------------
# Indexing works just like it did with strings:
# the first item is at index 0, and -1 is the last item.

print("\n--- Accessing Items ---")

print("First subject:", subjects[0])
print("Last subject:", subjects[-1])
print("First two subjects:", subjects[:2])


# ------------------------------------------------------------
# 3. LISTS CAN BE CHANGED
# ------------------------------------------------------------
# Unlike strings, a list can be modified after it is created.

print("\n--- Changing a List ---")

subjects.append("Electronics")        # add an item at the end
print("After append:", subjects)

subjects[0] = "Python 3"              # replace an item
print("After replacing index 0:", subjects)

subjects.remove("OS")                 # remove an item by value
print("After remove:", subjects)

marks = [72, 95, 58, 81]
marks.sort()                          # sort the list in place
print("Sorted marks:", marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Total:", sum(marks))


# ------------------------------------------------------------
# 4. LOOPING THROUGH A LIST
# ------------------------------------------------------------

print("\n--- Looping Through a List ---")

for subject in subjects:
    print("I am learning", subject)

print("Is 'C++' in the list?", "C++" in subjects)


# ------------------------------------------------------------
# 5. TUPLES
# ------------------------------------------------------------
# A tuple is like a list, but it CANNOT be changed after creation.
# Tuples use round brackets.
# Use a tuple for values that should stay fixed.

print("\n--- Tuples ---")

point = (10, 20)

print("Point:", point)
print("x =", point[0])
print("y =", point[1])

# Trying to change a tuple causes a TypeError.
try:
    point[0] = 99
except TypeError as error:
    print("Error:", error)

# Tuples can be "unpacked" into separate variables.
x, y = point
print("Unpacked ->", x, y)


# ------------------------------------------------------------
# YOUR TURN (EASY): LIST OF NUMBERS
# ------------------------------------------------------------
# Ask the user for 5 numbers and store them in a list.
# Then print the list, the largest number and the sum.
#
# Example:
#   Numbers entered: 4, 9, 2, 7, 5
#   List: [4, 9, 2, 7, 5]
#   Largest: 9
#   Sum: 27
#
# Hint: use append() to add each number, then max() and sum().

print("\n--- Your Turn: List of Numbers ---")

numbers = []

for i in range(5):
    value = int(input(f"Enter number {i + 1}: "))
    # TODO: add value to the numbers list


print("List:", numbers)
# TODO: print the largest number
# TODO: print the sum of all the numbers


# ------------------------------------------------------------
# BONUS CHALLENGE
# ------------------------------------------------------------
# 1. Print the numbers in reverse order using slicing.
# 2. Print only the numbers greater than 5.
# 3. Store a student's name and roll number in a tuple and
#    unpack it into two variables.
# ============================================================
