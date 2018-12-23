#While loop

#method 1 while loop
#i = 0
#numbers = []
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)     #put i into numbers

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
    
#     print("The numbers: ")

#     for num in numbers:
#         print(num)

#method 2 function
# numbers = []
# def while_loop(i, j, n):
#     if i < j:
#         print(f"At the top i is {i}")
#         numbers.append(i)     #put i into numbers
#         i = i + n 
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")
    
#         while_loop(i, j, n) 

# while_loop(0,6,2) 
# print("The numbers: ")
# for num in numbers:
#     print(num)   

#method 3 for range
numbers = []
for i in range(0, 6):
    if i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)     #put i into numbers
        # i = i + 1 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")    
print("The numbers: ")
for num in numbers:
    print(num)   