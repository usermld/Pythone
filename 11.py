n = int(input("fuf: "))
fib_1  = 1
fib_2  = 0
fib = 0
count = 1

while fib < n:
    fib = fib_1 + fib_2
    fib_2 = fib_1
    fib_1 = fib
    count += 1
    # print(fib)
    # print(fib_1)
    # print(fib_2)    
    
if fib != n:
    print(-1)
else:
    print(count)