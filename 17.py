# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.


import random

size = int(input("fuf: "))
list_1 = []

# for i in range(size):
#    num = random.randint(1, 5)
#    list_1.append(num)
# print(list_1)

list_1 = [random.randint(-5, 5) for i in range(size)]
print(list_1)


# print(len(set(list_1)))
# print(set(list_1))

res_list = []

for i in list_1:
    if i not in res_list:
        res_list.append(i)

#print(len(res_list))

[res_list.append(i) for i in list_1 if i not in res_list]

res_list_2 = [res_list.append(i) for i in range(len(list_1)) if list_1[i] not in list_1[i+1:]]
print(len(res_list_2))