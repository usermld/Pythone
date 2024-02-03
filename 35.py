def serch_simple_num (n):
    if n != 2 and n % 2 == 0:
        return "no"
    for div in range (3, int(n **0.5 ) + 1, 2):
        if n % div == 0:
            return "no"
    return "yes"
user_num = int(input("fuf: "))
print(serch_simple_num(user_num))