year = int(input("Введите год: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Yea")
else:
    print("Nah")