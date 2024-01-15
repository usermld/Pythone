# import math

# distance = int(input("Введите длину маршрута: "))
# speed = int(input("Введите скорость в день: "))
# day = math.ceil(distance / speed)
# print (day)


#2

distance = int(input("Введите длину маршрута: "))
speed = int(input("Введите скорость в день: "))
day = (distance + speed - 1) // speed
print (day)