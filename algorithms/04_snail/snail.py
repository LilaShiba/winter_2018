import random
def snail(arr):
    ans = []
    # first row
    while len(arr) > 0:
        ans += arr[0]
        del arr[0]
    # down
        if len(arr) > 0:
            for x in arr:
                ans += [x[-1]]
                del [x[-1]]
            # back
            if arr[-1]:
                ans += arr[-1][::-1]
                del arr[-1]
            # up again
            for i in reversed(arr):
                ans += [i[0]]
                del i[0]
    return(ans)
num = 5
meow = [[random.randint(0,10) for i in range(num)] for j in range(num)]
print('i am the 2d arr', meow)
ans = snail(meow)
print("i am the ans", ans)
