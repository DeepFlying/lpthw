#While loop
numbers = []
def while_loop(i, j):
    if i < j:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
        
        while_loop(i,j)    
while_loop(0,6) 
print("The numbers: ")
for num in numbers:
    print(num)   
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
    
#     print("The numbers: ")

#     for num in numbers:
#         print(num)
   