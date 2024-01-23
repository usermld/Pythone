list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0
i = 0

while i < len(list_1):
    if k == list_1[i]:
        count += 1
        i += 1
    else:
        i += 1
print(count)