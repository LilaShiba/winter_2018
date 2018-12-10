import time
start_time = time.clock()
def fib(n):
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

for n in range(1,100):
    print(n, ':', fib(n))
print(time.clock() - start_time, "seconds")
