from random import randint

n = int(input("fuf: "))

#max = 0  # float("inf")
#min = 0  # -float("inf")

for _ in range(n):
    temp = randint(1, 10000)
    print(temp, end =" ")
    
    max = temp
    min = temp
    
    if temp > max:
        max = temp
        
    if min > temp:
        min = temp
        
print()
print(f"max = {max}")
print(f"min = {min}")