#Stings and Text
# the number of  type of people
types_of_people = 10

# x is f-string 
x = f"There are {types_of_people} types of people."

#binary is a string variable
binary = "binary"

#do_not is a string variable
do_not = "don't"

# y is a string variable
y = f"Those who know {binary} and those who {do_not}."

#print string x
print(x)

#print string y
print(y)

#print a combined string with x
print(f"I said: {x}")

#print a combined string with y
print(f"I also said: '{y}'")

hilarious = "False"
#not known
joke_evaluation = "Isn't that joke so funny?! {}"

#print a format string
print(joke_evaluation.format(hilarious))

# w is a string variable
w = "This is the left side of ..."

#e is a string variable
e =  "a string with a right side."

#print a string which w and e are combined
print(w + e)
