# Python Program for recursive binary search.
# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
    # Check base case
    if r >= l:
        # dealing with index values
        mid = l + (r - l)//2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40, 100]
x = 100

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
