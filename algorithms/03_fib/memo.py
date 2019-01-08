import time
start_time = time.clock()

memo = {}
def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2)

    memo[n] = f
    return f

for n in range(1,100):
    print(n, ':', fib(n))
print(time.clock() - start_time, "seconds")
print(fib(100))
