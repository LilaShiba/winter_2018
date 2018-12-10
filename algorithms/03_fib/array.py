def fib(n):
    arr = [0 for x in range(n)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n):
        arr[i] = (arr[i -1] + arr[i - 2]) % 10
    return(arr[-1] % 10)
print(fib(80000))
