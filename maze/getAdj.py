
import random, pprint

matrix = [[random.randint(0,100) for col in range(5)] for row in range(5)]
def makeMatrix(row,col,start=0,stop=100):
  matrix = [[random.randint(start,stop)for col in range(col)]for row in range(row)]
  return matrix

test_case_1 = makeMatrix(10,10,1,110)
#pprint.pprint(test_case_1)
def getAdj(alist, n):
  x,y = n
  if x > 0:
    up = (x-1,y)
  else:
    up = -1

  if y > 0:
    left = (x,y-1)
  else:
    left = -2

  if x < len(alist) - 1:
    down = (x+1,y)
  else:
    down = -3

  if y < len(alist) -1:
    right = (x,y+1)
  else:
    right = -4

  return {up, right, down, left}

def makeAdj(alist,n):
  adj_list = {}
  for row in range(n):
    for col in range(n):
      temp_l = getAdj(alist,(row,col))
      #adj_list.append(temp_l)
      adj_list[(row,col)] = temp_l
  pprint.pprint(alist)
  pprint.pprint(adj_list)
  return adj_list


# make adjacency list based off matrix & cardinal directions
# makeAdj(matrix, 5)
my_adj_list = makeAdj(test_case_1, 10)
