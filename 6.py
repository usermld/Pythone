n = 987654
n1 = 0
n2 = 0
n1 = (n % 10) + ((n // 10) % 10)+ ((n // 100) % 10)
print(n1)
n //= 1000
print(n)
n2 = (n % 10) + ((n // 10) % 10)+ ((n // 100) % 10)
print(n2)
if n1 == n2:
    print("yes")
else:
    print("no")
