#Reading Files
#use argv to get user input
from sys import argv

#unpack the input
script, filename = argv

#open the file
txt = open(filename)

#print the filename
print(f"Here's your file {filename}:")

#print the file's content
print(txt.read())

#input a new file
print("Type the filename again:")

#input the file after >
file_again = input("> ")

#open the file
txt_again = open(file_again)

#print the file's content
print(txt_again.read())