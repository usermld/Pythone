def sum_div(num):
    summa = 1
    for div in range(2, num // 2 + 1):
        if num % div ==  0:
            summa += div
    return summa
    #return sum([div for div in range(2, num ) if num % div ==  0])        

k = int(input("fuf: "))

for num_1 in range(2, k + 1):
    num_2 = sum_div(num_1)
    if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 <= k:
        print(num_1, num_2)