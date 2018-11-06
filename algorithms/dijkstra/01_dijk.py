# https://www.youtube.com/watch?v=IG1QioWSXRI
# G = (V,E)
graph = {
        'a':{'b':10, 'c':3},
        'b':{'c':1, 'd':2},
        'c':{'b':4, 'd':8,'e':2},
        'd':{'e':7},
        'e':{'d':9}
        }

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

dijkstra(graph,'a','d')
