# # list_1 = [1,2,3,5,8,15,23,38]
# # list_2 = []
# # i = 0
# # while i < len(list_1):
# #     if list_1[i] % 2 == 0:
# #         list_2.append(f"({list_1[i]},")    
# #         list_2.append(f"{list_1[i] * list_1[i]})")
# #     i += 1
    
# # print(list_2)

# data = [1,2,3,5,8,15,23,38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
        
# print(res)

def select (f, col):
    return[f(x) for x in col]

def where (f, col):
    return[x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x **2), res))
print(res)