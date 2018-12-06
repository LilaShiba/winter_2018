import time

start_time = time.clock()
memo = {}
def fib(n):
    if n in memo: return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)

    memo[n] = f
    return f

for n in range(1,35):
    print(n, ':', fib(n))
print(time.clock() - start_time, "seconds")
