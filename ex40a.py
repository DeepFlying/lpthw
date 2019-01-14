#Modules, Classes, Objects
#method1
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

#method2
import mystuff
mystuff.apple()
print(mystuff.tangerine)

#method3
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)
