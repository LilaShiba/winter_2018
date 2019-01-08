def coin(n):
    count = 0
    while n > 0:
        if n >= 10:
            n -= 10
            count += 1
        elif n >= 5:
            n -= 5:
            count += 1
        else:
            n -= 1
            count += 1
    return count
