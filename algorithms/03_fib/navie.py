import time
start_time = time.clock()
def fib(n):
    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2)
    return f

# timing
for n in range(1,100):
    print(n, ':', fib(n))
print(time.clock() - start_time, "seconds")
