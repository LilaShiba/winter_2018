def find_neighbours(node, length):
    edges = []
    x,y = node
    for x,y in (x, y-1), (x, y+1), (x+1, y), (x-1, y):
        if 0 <= x < length and 0 <= y < length:
            edges.append(x,y)
    return edges


def bfs(graph):
    explored = []
    queue = [(0, 0)]]

    while queue:
        # get the last element of the queue
        node = queue.pop(0)
        # check if node has been explored
        if node not in explored:
            explored.append(node)
            neighbours = find_neighbours(node, length)
            # add all neighbours of the node to the queue
            for neighbour in neighbours:
                queue.append(neighbour)
