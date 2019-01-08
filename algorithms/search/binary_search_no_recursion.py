def binary_search(a, x):
    # floor floats
    mid = len(a)//2
    high = len(a)-1
    # no recursion, makes it harder to return idx
    while a[mid] != x:
        if mid == high:
            return -1
        # if mid is greater than value
        elif a[mid] > x:
            # half the arrary
            high = mid
            mid = (mid//2)
        # if mid is less than value
        elif a[mid] < x:
            # half the array
            mid = (mid+1+high)//2
    return mid
