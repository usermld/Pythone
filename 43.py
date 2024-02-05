from random import randint

size_n = int(input("fuf: "))

n = []

n = [randint (1, 5) for _ in range(size_n)]
print(n)

count = 0
for i in range(len(n)):
    # for j in range(i+1, len(n)):
    #     if n[i] == n[j]:
    #         count += 1
    count += n[i+1:].count(n[i])
    
print(count)    
    