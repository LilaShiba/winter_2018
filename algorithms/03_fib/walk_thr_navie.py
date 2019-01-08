
# memo = {}
def fib(n):
    # if n is in memo:
        #return n

    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2)
    # memo[n] = f
