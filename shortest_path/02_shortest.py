import pprint
a = "\n".join([
  ".W.",
  ".W.",
  "..."
])
def make_nested(n_list):
    a = n_list.split('\n')
    new_a = []
    for x in a:
        new_a.append(list(x))
    return new_a

maze = make_nested(a)

def get_adj(n_list, n):
    x,y = n
    if x > 0:
        up = (x-1, y)
    else:
        up = (x,y)

    if y > 0:
        left = (x, y-1)
    else:
        left = (x,y)

    if x < len(n_list) - 1:
        down = (x+1, y)
    else:
        down = (x,y)

    if y < len(n_list) - 1:
        right = (x, y+1)
    else:
        right = (x,y)

    return {up, right, down, left}

def make_adj_list(n_list):
    adj_list = {}
    for row in range(len(n_list)):
        for col in range(len(n_list)):
            if n_list[row][col] != 'W':
                tempL = get_adj(n_list, (row,col))
                adj_list[(row,col)] = tempL
            else:
                temp_r = row
                temp_c = col
                adj_list[(row,col)] = {(temp_r,temp_c)}
    return adj_list

adj_list = make_adj_list(maze)

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
    return "So sorry, but a connecting path does not exist"

ans = bfs_shortest_path(adj_list, (0,0), (2,2))
print(ans)
