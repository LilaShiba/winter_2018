graph = {
        'a':{'b':10, 'c':3},
        'b':{'c':1, 'd':2},
        'c':{'b':4, 'd':8,'e':2},
        'd':{'e':7},
        'e':{'d':9}
        }


def dijkstra(graph,start,stop):
    shortest_dist = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 99999999
    paths = []

    # set all nodes to infinity
    # copy from unseenNodes to populate shortest_dist
    for node in unseenNodes:
        shortest_dist[node] = infinity
    # start node is 0
    shortest_dist[start] = 0
    print(shortest_dist)

    # run until dict is empty
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            #first case
            if minNode is None:
                minNode = node

            elif shortest_dist[node] < shortest_dist[minNode]:
                minNode = node
    # check childNodes meow
        for childNode, weight in graph[minNode].items():
            if weight + shortest_dist[minNode] < shortest_dist[childNode]:
                shortest_dist[childNode] = weight + shortest_dist[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    print(shortest_dist)
    print(predecessor)
dijkstra(graph,'a','d')
