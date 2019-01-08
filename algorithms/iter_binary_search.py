def binary_search(a, low, high, key):
    while low <= high:
        mid = (low + (high-low)//2)
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1


import random
a = [random.randint(0,15) for x in range(15)]
print(a)
print(binary_search(a, 0, len(a), 8))
