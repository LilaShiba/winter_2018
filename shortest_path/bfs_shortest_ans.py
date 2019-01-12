#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
import pprint
a = "\n".join([
  ".W..",
  "....",
  ".W..",
  ".W.."
])

def find_neighbours(node,length, matrix):
  neighbours = []
  x, y = node
  for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
    if 0 <= x < length and 0 <= y < length:
        if matrix[x][y] == '.':
            neighbours.append([x,y])
  return neighbours

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    queue, length = [[(0, 0)]], len(matrix)
    explored = []
    goal = [length-1,length-1]
    #BFS
    while queue:
      # pop the first path from the queue
      path = queue.pop(0)
      # get the last node from the path
      node = path[-1]
      if node not in explored:
        neighbours = find_neighbours(node, length, matrix)
        for neighbour in neighbours:
          x,y = neighbour
          new_path = list(path)
          new_path.append(neighbour)
          queue.append(new_path)
          if neighbour == goal:
              return len(new_path)-1
        explored.append(node)
    return False

print(path_finder(a))
