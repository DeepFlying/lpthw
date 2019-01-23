#Inheritance versus Composition
class Parent(object):               #define a Parent class
    
    def override(self):             #define a override function
        print("PARENT override()")  #print a string

    def implicit(self):             #define a implicit function
        print("PARENT implicit()")  #print a string

    def altered(self):              #define a altered function
        print("PARENT altered()")   #print a string

class Child(Parent):                #define a Child class

    def override(self):             #define a override function
        print("CHILD override()")   #print a string

    def altered(self):              #define a altered function
        print("CHILD,BEFORE PARENT altered()")  #print a string
        super(Child, self).altered()            #use super to get parent.altered version
        print("CHILD, AFTER PARENT altered()")  #print a string

dad = Parent()      #instance
son = Child()       #instance

dad.implicit()      #call function
son.implicit()      #call function

dad.override()      #call function
son.override()      #call function

dad.altered()       #call function
son.altered()       #call function
