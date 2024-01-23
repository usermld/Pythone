from random import randint

n = int(input("fuf: "))

count = 0
max = 0

for i in range(n):
    temp = randint(-50, 50)
    print(temp, end =" ")
    if temp > 0:
        count += 1
        if count > max:
            max += count
    else:
        count = 0
        max += count
        
print()
print(f"max = {max}")


