from typing import List
from random import randint


def smallest_element_index(original_list):
    smallest_index = 0
    sm_element = original_list[smallest_index]
    for index in range(1, len(original_list)):
        if original_list[index] < sm_element:
            sm_element = original_list[index]
            smallest_index = index
    return smallest_index


def selection_sort(original_list):
    sorted_list = []
    for index in range(len(original_list)):
        # find the smallest element
        smallest_index = smallest_element_index(original_list)
        # add the element to the sorted list
        # remove the smallest from the origin list
        sorted_list.append(original_list.pop(smallest_index))
    return sorted_list


random_list = [randint(1, 100) for x in range(20)]
print(random_list)
print(selection_sort(random_list))