num_pixels = 55

def fib(n):
    if n <= 1:
        return n
    arr = [0 for x in range(n)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n):
        arr[i] = (arr[i -1] + arr[i - 2])
    return(arr[-1])

count = 0
light_range = 0
past_range = 0
while (light_range + past_range) < num_pixels:
    count += 1
    past_range = light_range
    light_range = fib(count)
    p_count = 0
    while p_count < light_range:

        p_count += 1
    print(p_count)
