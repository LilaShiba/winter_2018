# review for 1/7
import timeit
start = timeit.default_timer()
val = 2
arr = [1,2,3,4,5,6,7,8,9,10]

def ssearch(arr, val):
    count = -1
    for x in arr:
        count += 1
        if x == val:
            print(count)
        else:
            print(False )

ssearch(arr, val)


stop = timeit.default_timer()

print('Time: ', stop - start)
