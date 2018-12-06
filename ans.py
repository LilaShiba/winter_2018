# review for 12/5
import time
start_time = time.clock()
matrix = [[98, 19, 1, 46, 51, 33, 3, 33, 80, 40], [26, 88, 79, 10, 63, 76, 18, 49, 47, 44], [18, 53, 8, 96, 40, 53, 73, 8, 31, 43], [8, 40, 31, 98, 19, 39, 15, 9, 58, 32], [76, 45, 1, 5, 15, 14, 20, 88, 51, 48], [11, 13, 15, 46, 50, 56, 23, 21, 83, 23], [47, 62, 69, 9, 88, 16, 97, 28, 50, 64], [61, 50, 18, 24, 100, 15, 91, 31, 81, 57], [38, 73, 90, 82, 0, 26, 81, 38, 34, 21], [86, 94, 27, 22, 38, 88, 78, 1, 80, 56]]
# planning ahead! What am I returning?
h_even = 0
h_odd = 0
# nested loop
for row in range(len(matrix)):
    #
    for col in range(len(matrix)):
        # if statement for even
        if matrix[row][col] % 2 == 0:
            if matrix[row][col] > h_even:
                h_even = matrix[row][col]
        #else:
        #    if matrix[row][col] > h_odd:
        #        h_odd = matrix[row][col]
print(h_even)


print(time.clock() - start_time, "seconds")
