# same time as linear
def find_max(li, left, right):
    # base case
    if left == right:
        return li[left]

    mid = int((left + right) / 2)

    max1 = find_max(li, left, mid)
    max2 = find_max(li, mid+1, right)
    print(max1 if max1 > max2 else max2)
    return max1 if max1 > max2 else max2

arr = [10,24,2,122,546,343,231,434,10000,10,100]


find_max(arr, 0, len(arr)-1)
