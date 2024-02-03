def revers (num):
    el = input("fif: ")
    if num == 1:
       return print(el, end = " ")
    revers(num-1)
    print(el, end = " ")
    
    

n = int(input("fuf: "))
print(revers(n))