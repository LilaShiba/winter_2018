arr = [ [10, 10, 34],
        [11, 100, 12],
        [11, 10, 14] ]

#print(arr[1][1])
#print(arr[2][2])

sum = 0
n = 1

# add one col together
for x in range(0,3):
    sum = sum + (arr[x][n])
print(sum)

# total (N)
# // if N (column number) is not passed as an input parameter then
# // assignment must appear in pseudocode, for example, N = input()
#   SUM = 0
#   loop for WEEK from 0 to 29
#       SUM = SUM + 2D_ARRAY[WEEK][N]
#   end loop
#   return SUM
# end total
