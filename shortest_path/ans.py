def make_nested(n_list):
    a = n_list.split('\n')
    new_a = [list(x) for x in a]
    return new_a



def get_adj(n_list, n):

    x,y = n
    ans = []

    if n_list[x][y] != 'W':
        if x > 0:
            up = (x-1, y)
            ans.append(up)
        if x < len(n_list) - 1:
            down = (x+1, y)
            ans.append(down)

        if y < len(n_list) - 1:
            right = (x, y+1)
            ans.append(right)
        if y > 0:
            left = (x, y-1)
            ans.append(left)

    return ans



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
    print(ans)
a = "\n".join([
  ".W.",
  ".W.",
  "...",
  ".W."
])
path_finder(a)
