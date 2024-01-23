'''
Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
количество элементов массива, больших предыдущего (элемента с предыдущим номером)


Input: [0, -1, 5, 2, 3]


Output: 2

Пояснение: (-1 < 5, 2 < 3)


Примечание: Пользователь может вводить значения списка или список задан изначально.
'''

from random import randint

size = int(input("fuf: "))
numbers = []

for _ in range(size):
    numbers.append(randint(-5, 5))
print(numbers)

numbers = [randint(-5, 5) for _ in range(size) ]


count = 0
i = 0
i_1 = 1

while i_1 < size:
    if numbers[i] > numbers[i_1]:
        count += 1
        i += 1
        i_1 += 1
    else:
        i += 1
        i_1 += 1

print(count)