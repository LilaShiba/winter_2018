import random
# 2d array list compression & control % of non obstacle path
adjacency_list = [[random.randint(0,3) for col in range(10)] for row in range(10) ]
# datatype to string
def make_map(adjacency_list):
    for row in range(len(adjacency_list)):
        for col in range(len(adjacency_list)):
            if adjacency_list[row][col] == 1:
                adjacency_list[row][col] = 'i'
            else:
                adjacency_list [row][col] = 'o'
    print(adjacency_list)
    return(adjacency_list)
# call and declare adjacency_list
adjacency_list = make_map(adjacency_list)

def find_it(matrix):
    # declare stack
    stack, length = [[0, 0]], len(matrix)
    # run until empty
    while len(stack):
      x, y = stack.pop()
      print(x, y)
      # mark visited
      if matrix[x][y] == 'o':
        matrix[x][y] = 'x'
        # try cardinal directions
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    return matrix[length-1][length-1] == 'x'
# test path from top left to bottom right
print(find_it(adjacency_list))
