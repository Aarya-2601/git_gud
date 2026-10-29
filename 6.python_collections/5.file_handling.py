# ============================================================
# PYTHON COLLECTIONS: FILE HANDLING
# ============================================================
# In this file, we will learn:
# 1. Opening files and the with statement
# 2. File modes: "w", "r" and "a"
# 3. Writing to a file
# 4. Reading from a file
# 5. Append vs overwrite
# 6. Your turn: two small interactive tasks
#
# NOTE: Run this file from inside the 6.python_collections folder.
# The files it creates will appear in that same folder.
# ============================================================


# ------------------------------------------------------------
# 1. OPENING FILES
# ------------------------------------------------------------
# open(filename, mode) gives us access to a file.
#
# Modes:
#   "w"  write   - creates the file, ERASES anything already inside
#   "r"  read    - reads an existing file
#   "a"  append  - adds to the end without erasing
#
# Always use the with statement. It closes the file for us,
# even if something goes wrong.


# ------------------------------------------------------------
# 2. WRITING TO A FILE
# ------------------------------------------------------------

with open("file_demo.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")

print("File written!")

# \n means "new line". write() does not add one for us.


# ------------------------------------------------------------
# 3. READING A FILE
# ------------------------------------------------------------

print("\n--- read() ---")

with open("file_demo.txt", "r") as f:
    content = f.read()

print(content)

print("--- readlines() ---")

with open("file_demo.txt", "r") as f:
    lines = f.readlines()

print(lines)

print("--- looping line by line ---")

with open("file_demo.txt", "r") as f:
    for line in f:
        print("Got:", line.strip())


# ------------------------------------------------------------
# 4. APPEND VS OVERWRITE
# ------------------------------------------------------------

print("\n--- Append ---")

with open("file_demo.txt", "a") as f:
    f.write("Line three\n")

with open("file_demo.txt", "r") as f:
    print(f.read())

print("--- Overwrite ---")

with open("file_demo.txt", "w") as f:
    f.write("Only this line is left\n")

with open("file_demo.txt", "r") as f:
    print(f.read())

# "a" keeps what is already in the file. "w" wipes it first.
# Mixing them up is one of the most common beginner bugs.


# ------------------------------------------------------------
# YOUR TURN (EASY): GREETING FILE
# ------------------------------------------------------------
# Ask for the user's name. Write "Hello, <name>" to greeting.txt,
# then read the file back and print what is inside.
#
# Example:
#   Enter your name: Asha
#   Hello, Asha

print("\n--- Your Turn: Greeting File ---")

name = input("Enter your name: ")

# TODO: open greeting.txt in write mode and write "Hello, <name>"

# TODO: open greeting.txt in read mode and print its contents


# ------------------------------------------------------------
# YOUR TURN (MEDIUM): MINI DIARY
# ------------------------------------------------------------
# Keep asking the user for a line of text until they type "quit".
# Save every line to diary.txt, one per line, then print the
# whole diary.
#
# IMPORTANT: run the program twice. The lines from your first
# run must still be in the file during the second run!
#
# Hint: which mode keeps old content, "w" or "a"?

print("\n--- Your Turn: Mini Diary ---")

while True:
    line = input("Write a line (or 'quit'): ")

    if line == "quit":
        break

    # TODO: open diary.txt in the right mode and write the line
    #       (remember to add "\n" at the end)


print("\n--- Your Diary ---")

# TODO: open diary.txt in read mode and print everything in it


# ------------------------------------------------------------
# BONUS CHALLENGE
# ------------------------------------------------------------
# 1. Count how many lines are in diary.txt.
# 2. Print only the lines that contain a word of your choice.
# 3. Handle the case where the file does not exist yet
#    (hint: try / except FileNotFoundError).
# ============================================================
