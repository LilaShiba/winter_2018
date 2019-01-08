def fib(n):
    if n <= 1:
        return n
    arr = [0 for x in range(n)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n):
        arr[i] = (arr[i -1] + arr[i - 2])
    return(arr[-1])
print(fib(0))
