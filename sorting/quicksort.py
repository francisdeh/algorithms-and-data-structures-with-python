from random import randint


def qsort(ls):
    """ Worst case if you pick the pivot in first index for an already sorted array. Much faster if middle is picked
    for sorted array. O(nlogn) """
    if len(ls) < 2: return ls
    pivot = ls[0]
    less = [x for x in ls[1:] if x <= pivot]
    greater = [x for x in ls[1:] if x > pivot]
    return qsort(less) + [pivot] + qsort(greater)


random_list = [randint(1, 100) for x in range(20)]
print(random_list)
print(qsort(random_list))
