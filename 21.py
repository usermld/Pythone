'''
Задача №21. Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


Примечание: Список словарей задан изначально. Пользователь его не вводит
'''

lists_dickts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}, {"VIII":"S057"}]

unique = set()

for cur_dictk in lists_dickts:
    for value in cur_dictk.values():
        unique.add(value)
        
print(unique)

# unique = set()

# for cur_dictk in lists_dickts:
#     unique.add(*cur_dictk.values())
    
# print(unique)

unique = set()

for cur_dictk in lists_dickts:
    unique.update(cur_dictk.values())
    
print(unique)