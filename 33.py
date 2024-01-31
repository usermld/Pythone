from random import randint 

def max2min (numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    while max_num in numbers:
        i_max_num = numbers.index(max_num)
        numbers[i_max_num] = min_num



n = int(input("fuf: "))
marks = []

for _ in range(n):
    marks.append(randint(1,5))
    
print(marks)

# marks = [randint(1,5) for _ in range(n)]

# print(marks)
max2min(marks)
print(marks)