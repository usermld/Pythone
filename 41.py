from random import randint

size_n = int(input("fuf: "))

n = []

n = [randint (1, 5) for _ in range(size_n)]
print(n)

count = 0

for i in range(1, len(n) -1):
    if n[i-1] < n[i] > n[i+1]:
        count += 1
        
print(count) 
 