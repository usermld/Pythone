a = 12
b = 27

# i = 1

# while p % i == 0:
#     i += 1
#     print(i)
# print(i)



# min = 0
# max = 15

# while max * min != p:
#     max -= 1
#     min += 1
#     if min == -5:
#         break
#     print(max, min)
    
# print("min, max")

#a, b = map(int, input().split())
res = []
for i in range(a + b):
    if i == (a * i - b)**0.5:
        res.append(i)
print(*res if len(res) == 2 else res + res)
