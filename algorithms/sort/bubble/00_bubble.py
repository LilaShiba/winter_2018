def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # traverse the array from 0 to n-i-1
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            # Swap if the element found is greater
            # than the next element
        if swap == False:
            break
        print(arr)

arr = [1,100,2,1,4]
bubbleSort(arr)
