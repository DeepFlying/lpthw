#is-a(是什么), has-a(有什么), objects, and classes
##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal 
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute named name 
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute named name
        self.name = name
    
## Person is-a object
calss Person(object):

    def __init__(self, name):
        ## Person has-a attribute named name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

## Employee has-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Cat is-a Satan
satan = Cat("Satan")

## Person has-a Mary
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## Frank has 120000 employee
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## 
flipper = Fish()

 ## ??
crouse = Salmon()

## ??
harry = Halibut()


