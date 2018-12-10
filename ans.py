# review for 12/5
import timeit
start = timeit.default_timer()

matrix = [[98, 19, 1, 46, 51, 33, 3, 33, 80, 40], [26, 88, 79, 10, 63, 76, 18, 49, 47, 44], [18, 53, 8, 96, 40, 53, 73, 8, 31, 43], [8, 40, 31, 98, 19, 39, 15, 9, 58, 32], [76, 45, 1, 5, 15, 14, 20, 88, 51, 48], [11, 13, 15, 46, 50, 56, 23, 21, 83, 23], [47, 62, 69, 9, 88, 16, 97, 28, 50, 64], [61, 50, 18, 24, 100, 15, 91, 31, 81, 57], [38, 73, 90, 82, 0, 26, 81, 38, 34, 21], [86, 94, 27, 22, 38, 88, 78, 1, 80, 56]]
# planning ahead! What am I returning?
# nested loop
count = 0
sum = 0
for row in matrix:
    sum = sum + matrix[count][count]
print(sum)

stop = timeit.default_timer()

print('Time: ', stop - start)
