# https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
import random
# 2d array list compression & control % of non obstacle path
adjacency_list = [[random.randint(0,2) for col in range(4)] for row in range(4) ]
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
matrix = make_map(adjacency_list)
matrix[-1][-1] = 'x'

def search(x, y, grid):
    if grid[x][y] == 'x':
        print('found at %d,%d' % (x, y,))
        return True
    elif grid[x][y] == 'i':
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False

    print('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y, grid))
        or (y > 0 and search(x, y-1, grid))
        or (x > 0 and search(x-1, y, grid))
        or (y < len(grid)-1 and search(x, y+1, grid))):
        return True

    return False



print(search(0, 0, matrix))
