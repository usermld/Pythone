list_1 = [1, 2, 3, 4, 6]
k = 6
# i = 0
# j = 1
# count = 0
# count_2 = 0


# while i < len(list_1):
#     count = k - list_1[i]
#     count_2 = k - list_1[j]
    
#     if count < 0:
#         count *= -1
#     if count_2 < 0:
#         count_2 *= -1
    
#     i += 1

def closest(list_1, k):
     
    return list_1[min(range(len(list_1)), key = lambda i: abs(list_1[i]-k))]
print(closest(list_1, k))