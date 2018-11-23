from sys import argv

#ubpack the user's input
script, filename = argv

#print the filename
print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

#wait for the command 
input("?")

print("Opening the file...")

#open the file with a command write
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")

#clean the file's content
target.truncate()

print("Now I'm going to ask you for three lines.")
#input three line
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#write three into file
target.write(line1+"\n"+line2+"\n"+line3+"\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
#close the file
target.close()
