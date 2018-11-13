import random, pprint
# work on making true shortest path by addressing loops
def makeMatrix(row,col,start=1,stop=9):
  matrix = [[random.randint(start,stop)for col in range(col)]for row in range(row)]
  return matrix
# a nxn matrix
test_case_1 = makeMatrix(10,12)

# make random walls
def make_walls(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] < 3:
                matrix[row][col] = 0
    return matrix

test_case_1 = make_walls(test_case_1)

# get basic 4 directions as edges
def getAdj(alist, n):
  x,y = n
  if x > 0:
    up = (x-1,y)
  else:
    up = (x,y)

  if y > 0:
    left = (x,y-1)
  else:
    left = (x,y)

  if x < len(alist) - 1:
    down = (x+1,y)
  else:
    down = (x,y)

  if y < len(alist) -1:
    right = (x,y+1)
  else:
    right = (x,y)

  return {up, right, down, left}

# make adj list
def makeAdj(alist,n):
  adj_list = {}
  for row in range(n):
    for col in range(n):
        if alist[row][col] != 0:
            temp_l = getAdj(alist,(row,col))
            adj_list[(row,col)] = temp_l
        else:
            temp_r = row
            temp_c = col
            adj_list[(row,col)] = {(temp_r,temp_c)}
  #pprint.pprint(alist)
  #pprint.pprint(adj_list)
  return adj_list

my_adj_list = makeAdj(test_case_1, 10)

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

# save shortest path ans
ans = bfs_shortest_path(my_adj_list, (0,0), (9,9))
# print out path in matrix
if ans == "So sorry, but a connecting path doesn't exist :(":
    print("So sorry, but a connecting path doesn't exist :(")
else:
    for x in ans:
        row = x[0]
        col = x[-1]
        test_case_1[row][col] = ''
    pprint.pprint(test_case_1)
