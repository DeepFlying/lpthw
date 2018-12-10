#What If
people = 20
cats = 30
dogs = 15

if people < cats:
    print("people < cats:")
    print("Too many cats! The world is doomed!\n")

if people > cats:
    print("people > cats:")
    print("Not many cats! The world is saved!\n")

if people < dogs:
    print("people < dogs:")
    print("The world is drooled on!\n")

if people > dogs:
    print("people > dogs:")
    print("The world is dry!\n")

dogs += 5

if people >= dogs:
    print("people >= dogs:")
    print("People are greater than or equal to dogs.\n")

if people <= dogs:
    print("people <= dogs:")
    print("People are less than or equal to dogs.\n")

if people == dogs:
    print("people == dogs:")
    print("People are dogs.\n")
