first_class = int(input("Кол-во человек в 1ом кабинете: "))
second_class = int(input("Кол-во человек во 2ом кабинете: "))
third_class = int(input("Кол-во человек в 3ем кабинете: "))

quanity_desk = ((first_class + 1) // 2) + ((second_class + 1) // 2) + ((third_class + 1) // 2)
print(f"Всего парт необходимо {quanity_desk}")
