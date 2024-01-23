n = int(input("Ввдеите изначальное число: "))

factorial = 1
#count = 2

while n > 1:
    factorial *= n
    n -= 1

print(factorial)
