# https://forum.freecodecamp.org/t/python-slice-start-stop-step/19202
# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation

import random

arr = random.sample(range(0,100),10)

# arr[start:end:step]
# start through, not past end, by step

# print value in reverse
for item in arr[::-1]:
    print("I am the value", item)

# print index
print('\n')
print('start of index\n')
for idx in range(len(arr)):
    print(idx)

# print index in reverse
print('\n')
print('start of reverse index\n')
for idx in range(len(arr[::-1])):
    print(idx)
