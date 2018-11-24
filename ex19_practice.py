def monkey_and_lucky(monkey):
    print("How monkeys do you have?")
    print(f"I have {monkey} monkeys.")
    print(f"Good luck to you, you will have {10*monkey} luckys.")
    print("Oh, my God, God bless you!\n")

print("We can just give the function numbers dirctly:")
monkey_and_lucky(10)

print("We can use some variables:")
amount_of_monkey = int(input("How monkeys do you have?\n"))
monkey_and_lucky(amount_of_monkey)

print("We can also use math inside:")
monkey_and_lucky(amount_of_monkey*10)

