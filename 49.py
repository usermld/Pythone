'''
2) - Дан список размеров(длина, ширина) эллипсов
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
- Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
'''

from math import pi

# def find_farthest_orbit(list_of_orbits):
#     s_max = 0
#     for a, b in list_of_orbits:
#         if a != b:
#             s = pi*a*b
#             if s > s_max:
#                 s_max = s
#                 a_b = a, b
#     return a_b
                
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# def find_farthest_orbit(list_of_orbits):
#     list_of_elips = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]
#     list_of_areas = [a*b*pi for a, b in list_of_elips]
#     max_area = max(list_of_areas)
#     i_max_area = list_of_areas.index(max_area)
#     return list_of_elips[i_max_area]
                
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits):
    list_of_elips = list(filter(lambda a_b: a_b[0] != a_b[1],list_of_orbits))
    list_of_areas = list(map(lambda a_b: pi * a_b[0] * a_b[1], list_of_elips))
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_elips[i_max_area]
                
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))