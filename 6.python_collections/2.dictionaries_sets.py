# ============================================================
# PYTHON COLLECTIONS: DICTIONARIES AND SETS
# ============================================================
# In this file, we will learn:
# 1. Dictionaries (key-value pairs)
# 2. Adding, updating and deleting entries
# 3. Looping through a dictionary
# 4. Sets (unique values only)
# 5. Set operations
# 6. Your turn: a small interactive task
# ============================================================


# ------------------------------------------------------------
# 1. DICTIONARIES
# ------------------------------------------------------------
# A dictionary stores data as key: value pairs.
# Think of a phone book: the name is the key, the number is the value.
# Dictionaries use curly brackets.

student = {
    "name": "Aarav",
    "age": 18,
    "branch": "Computer",
}

print("Student:", student)
print("Name:", student["name"])

# get() is a safer way to look something up.
# If the key does not exist, it returns a default instead of an error.
print("Phone:", student.get("phone", "not found"))


# ------------------------------------------------------------
# 2. ADDING, UPDATING AND DELETING
# ------------------------------------------------------------

print("\n--- Changing a Dictionary ---")

student["phone"] = "98765"       # add a new key
student["age"] = 19              # update an existing key
del student["branch"]            # delete a key

print("Updated student:", student)
print("Is 'name' a key?", "name" in student)


# ------------------------------------------------------------
# 3. LOOPING THROUGH A DICTIONARY
# ------------------------------------------------------------

print("\n--- Looping Through a Dictionary ---")

for key, value in student.items():
    print(key, "->", value)

print("All keys:", list(student.keys()))
print("All values:", list(student.values()))


# ------------------------------------------------------------
# 4. SETS
# ------------------------------------------------------------
# A set stores UNIQUE values only. Duplicates are removed
# automatically, and the order is not guaranteed.

print("\n--- Sets ---")

numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)

print("List with duplicates:", numbers)
print("Set without duplicates:", unique_numbers)

unique_numbers.add(10)
print("After add:", unique_numbers)


# ------------------------------------------------------------
# 5. SET OPERATIONS
# ------------------------------------------------------------

print("\n--- Set Operations ---")

a = {"python", "c", "math"}
b = {"python", "math", "os"}

print("Both (intersection):", a & b)
print("Either (union):", a | b)
print("Only in a (difference):", a - b)
print("Only in one of them:", a ^ b)


# ------------------------------------------------------------
# YOUR TURN (MEDIUM): WORD COUNTER
# ------------------------------------------------------------
# Ask the user for a sentence. Build a dictionary that counts
# how many times each word appears, then print it.
#
# Example:
#   Sentence: to be or not to be
#   Result:   {'to': 2, 'be': 2, 'or': 1, 'not': 1}
#
# Hint: counts.get(word, 0) gives the current count, or 0
# if the word has not been seen yet.

print("\n--- Your Turn: Word Counter ---")

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

counts = {}

for word in words:
    # TODO: increase the count of this word by 1 in the counts dictionary
    pass

print(counts)


# ------------------------------------------------------------
# BONUS CHALLENGE
# ------------------------------------------------------------
# 1. Print the word that appears the most times.
# 2. Use a set to print how many different words there are.
# 3. Ask for two sentences and print the words they share.
# ============================================================
