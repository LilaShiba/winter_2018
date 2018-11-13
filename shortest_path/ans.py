def make_nested(n_list):
    a = n_list.split('\n')
    new_a = [list(x) for x in a]
    return new_a


def get_adj(n_list, n):
    x,y = n
    if x > 0 and n_list[x][y] != 'W':
        up = (x-1, y)
    else:
        up = (x,y)

    if y > 0 and n_list[x][y] != 'W':
        left = (x, y-1)
    else:
        left = (x,y)

    if x < len(n_list) - 1 and n_list[x][y] != 'W':
        down = (x+1, y)
    else:
        down = (x,y)

    if y < len(n_list) - 1 and n_list[x][y] != 'W':
        right = (x, y+1)
    else:
        right = (x,y)

    return {up, right, down, left}



def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = get_adj(graph, node)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return len(new_path) - 1

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return False

def path_finder(a):
    maze = make_nested(a)
    num = len(maze[0]) - 1
    ans = bfs_shortest_path(maze, (0,0), (num,num))
    return ans
