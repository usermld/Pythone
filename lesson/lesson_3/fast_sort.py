def quik_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quik_sort(less) + [pivot] + quik_sort(greater)

print(quik_sort([12, 213, 123, 213]))