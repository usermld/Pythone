list_1 = [1, 2, 3, 4, 5]
list_2 = []
list_3 = []
k = 6
i = 0

while i < len(list_1):
    if k <= list_1[i]:
        list_1[i].add(list_2)
        i += 1
    else:
        list_1[i].add(list_3)
        i += 1
        