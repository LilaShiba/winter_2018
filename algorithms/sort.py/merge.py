# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

#MergeSort(arr[], l,  r)
#If r > l
#     1. Find the middle point to divide the array into two halves:
#             middle m = (l+r)/2
#     2. Call mergeSort for first half:
#             Call mergeSort(arr, l, m)
#     3. Call mergeSort for second half:
#             Call mergeSort(arr, m+1, r)
#     4. Merge the two halves sorted in step 2 and 3:
#             Call merge(arr, l, m, r)


def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # if the value of l is < value of R
            if L[i] < R[j]:
                # that index value is meow L[i]
                arr[k] = L[i]
                i+=1
            else:
                # or the other way around
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

        print(arr)


import random
my_arr = [random.randint(0,100) for x in range(10)]
mergeSort(my_arr)
