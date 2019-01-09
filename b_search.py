# create the b_search function
def b_search(arr, val):
    # find the mid of the arr
    mid = len(arr)//2
    # end case if val is found
    if val == arr[mid]:
        return True
    # cond if mid is greater than val
    elif val < arr[mid]:
        b_search(arr[:len(arr)//2], val)
    # cond if mid is less than val
    else:
        b_search(arr[len(arr)//2+1:], val)
# call our function
my_nums = list(range(100, 100000))
target = 16

print(b_search(my_nums, target))

# logic
def b_search_w(arr, val):
    mid = len(arr)//2
    high = len(arr) - 1

    while mid != val:
        # condition for if val is not in the list

        # condition for if val greater than the mid item
            # change value of mid, high, or both!
        # if val less than the mid item
            # change value of mid, high, or both!



        if mid == high:
            return False
        elif val > arr[mid]: # val is greater than mid
            mid = half of the upper half of arr
        else: # val is less than mid
            change mid to half of the lower half of arr
            change high to the new highest value
    return mid
