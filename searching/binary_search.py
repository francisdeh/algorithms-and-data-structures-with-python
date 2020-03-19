"""
Binary search accepts a list and the item to find
"""
from math import log


def binary_search(item_list, item):
    print("Worst case search", log(len(item_list), 2))
    print("Item to Search", item)
    count = 1
    # find the lowest index
    low = 0
    print("low  index", low)
    # find the highest index
    high = len(item_list) - 1
    print("high index", high)
    # whiles we are still within the range of the item list,
    # find the position of the number
    while low <= high:
        print("----A running search---- " + str(count))
        # get the middle index
        mid = (low + high) / 2
        print("middle index", mid)
        # guess item in the middle index
        guess = item_list[mid]
        print("Guessed item", guess)

        # if guessed item is the item we are looking for, return the position
        if guess == item:
            print("Guessed item is equal to item", guess == item)
            return mid
        # if the guessed item is greater than the item we are looking for,
        # discard the rest of the list from middle to the last(highest)
        # change the high to the middle element - 1
        if guess > item:
            high = mid - 1
            print("Guessed item is greater than item", guess > item)
            print("New high index is ", high)
            print("Low index is ", low)
            count += 1
        # else if the guessed item is lower than the item we are looking for,
        # discard the middle list to the lowest list,
        # change the low to be middle index + 1
        else:
            low = mid + 1
            print("Guessed item is lower than item", guess < item)
            print("New low index is ", low)
            print("High index is ", high)
            count += 1
    # if we dont find the position of the element, return None - null
    return None


# List of numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# item to search is 7
print("Position", binary_search(my_list, 7))  # prints 6
