from random import randint

size_n = int(input("fuf: "))
size_m = int(input("fif: "))
n = []
m = []

# for _ in range(size_n):
#     n.append(randint(-5, 10))

n = [randint(-5, 1000) for _ in range(size_n)]
print(n)
    
# for _ in range(size_m):
#     m.append(randint(-5, 10))
    
m = {randint(-5, 1000) for _ in range(size_m)}
print(m)


# res_list = []
# for num in n:
#     if num not in m:
#         res_list.append(num)
#         print(num, end= " ")
        
res_list = [num for num in n if num not in m]
print(*res_list)