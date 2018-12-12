#While loop
i = 0
numbers = []
def while_loop(i, j):
    if i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = j
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
        print("The numbers: ")

        for num in numbers:
            print(num)
        while_loop(i)    
while_loop(i,5) 
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
    
#     print("The numbers: ")

#     for num in numbers:
#         print(num)
        