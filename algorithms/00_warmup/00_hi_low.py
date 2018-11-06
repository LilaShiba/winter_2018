# You are given a string of space separated numbers,
# and have to return the highest and lowest number.


def hi_low(str):
    new_arr = []
    num = str.split()

    # turn str into list of ints
    for x in num:
        new_arr.append(int(x))
    print(new_arr)

    # return highest
    highest = 0
    for x in new_arr:
        if x > highest:
            highest = x
    print(highest)

    # return lowest
    lowest = highest
    for x in new_arr:
        if x < lowest:
            lowest = x
    print(lowest)


hi_low('400 20 200 800')
