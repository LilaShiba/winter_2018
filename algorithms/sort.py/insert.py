import random
arr = [random.randint(0,100) for x in range(10)]

def intSort(arr):
    # traverse from 1 - len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # move what is greater than ahead of key
        # j is behind key
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    return arr

print(intSort(arr))
