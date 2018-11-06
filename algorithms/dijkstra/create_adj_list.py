import random, pprint

def makeMatrix(row,col,start=0,stop=100):
  matrix = [[random.randint(start,stop)for col in range(col)]for row in range(row)]
  return matrix

test_case_1 = makeMatrix(10,10,11,99)

def make_walls(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] < 30:
                matrix[row][col] = 0
    return matrix

test_case_1 = make_walls(test_case_1)
#pprint.pprint(test_case_1)


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

  return {up: 1, right: 1, down: 1, left: 1}

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


# make adjacency list based off matrix & cardinal directions
# makeAdj(matrix, 5)
my_adj_list = makeAdj(test_case_1, 10)
print(my_adj_list)
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    # set all nodes to infinity
    # copy from unseenNodes to populate shortest_distance
    for node in unseenNodes:
        shortest_distance[node] = infinity
    # start node should be 0
    shortest_distance[start] = 0
    print(shortest_distance)

    # run until dict is empty
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            # first case
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        # check childnodes meow
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                # relax distance at childNode
                shortest_distance[childNode] =  weight + shortest_distance[minNode]
                # how it got there
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    # print(shortest_distance)
    # print(predecessor)

    # print path
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('path not found')
            break

    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print("shortest path is " + str(shortest_distance[goal]))
        print("the path is " + str(path))

dijkstra(my_adj_list,(1,1),(14,14))
