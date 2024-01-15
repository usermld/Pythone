count = int(input("Введите номер вагона в который сел гг: "))
number = int(input("Введите номер вагона поезда: "))
if count == number:
    print(f"нет инфы")
else:
    print(f"№ вагона {count + number - 1}")
