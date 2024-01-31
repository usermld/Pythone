'''
Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''

string = "a a a b c a a d c d d"
my_list = string.split()
dict_count = {}

for i in my_list:
    if i not in dict_count:
        print(i, end = " ")
        dict_count[i] = 0
    else:
        dict_count[i] += 1
        print(F"{i}_{dict_count[i]}", end = " ")
#print(dict_count)