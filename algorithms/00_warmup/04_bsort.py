# For a walk through
# http://zabana.me/notes/algorithms-in-python-bubble-sort.html
import random
def bsort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            # see swap.py if this is confusing
    print(arr)

arr = random.sample(range(0,100), 10)
print('here is the unsorted arr \n', arr)
print('\n')
print('here is the list sorted')
bsort(arr)
