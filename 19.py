# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

n = int(input("fuf: "))

list_ = [i for i in range(1, n+1)]
print(list_)
k = int(input("ufu: "))
print(list_[-k:] + list_[:-k])

for _ in range(k):
    les_ = list_.pop()
    list_.insert(0, les_)
print(list_)