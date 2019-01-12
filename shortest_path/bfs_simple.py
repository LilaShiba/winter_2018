#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
import pprint
a = "\n".join([
  ".W..",
  "....",
  ".W.W",
  ".W.."
])

def find_neighbours(node,length):
  neighbours = []
  x, y = node
  for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
    if 0 <= x < length and 0 <= y < length:
      neighbours.append([x,y])
  return neighbours

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    queue, length = [[0, 0]], len(matrix)
    explored = []
    #BFS
    while queue:
      # pop the first path from the stack
      node = queue.pop(0)

      if node not in explored:
        explored.append(node)
        neighbours = find_neighbours(node, length)
        for neighbour in neighbours:
          x,y = neighbour
          if matrix[x][y] == '.':
            matrix[x][y] = 'x'
          queue.append(neighbour)
    return matrix[length-1][length-1] == 'x'
print(path_finder(a))
