#from system import argv
from sys import argv

#unzip the argv
script, input_file = argv

#define a function can print all text's content
def print_all(f):
    print(f.read())

#rewind?
def rewind(f):
    f.seek(0)

#define a function can print the text's one line a time
def print_a_line(line_count, f):
    print(line_count, f.readline())

#open the file and given current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
