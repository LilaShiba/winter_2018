# For a walk through
# http://zabana.me/notes/algorithms-in-python-bubble-sort.html
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # traverse the array from 0 to n-i-1
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            # see swap.py if this is confusing
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    print(arr)

bubbleSort([1,5,4,3,2,8,7,10,9])
