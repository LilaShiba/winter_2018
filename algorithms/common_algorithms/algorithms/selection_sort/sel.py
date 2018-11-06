import random
def sel(arr):
    for i in range(len(arr)):
        min_pos = i
        # i + 1 = start pos
        for j in range(i+1, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
        # swap the smallest pos to the lowest index val
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp
    return arr

    
arr_test = [random.randint(0,10000) for x in range(10)]
print(sel(arr_test))
