from random import randint
def sort(n, m):
    i = 0
    while i < n:
        var2 = randint(-10, 10)
        print(f"{var2}", end = ', ')
        i += 1
    
    i = 0
    while i < m:
        var3 = randint(-10, 10)
        i += 1
        print(var3)
    print(var2, var3)
    
a  = 2
v = 4
sort(a, v)