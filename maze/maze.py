import random, pprint
matrix = [[random.randint(0,2) for col in range(5)] for row in range(5)]


def maze_maker(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] % 2 == 0:
                matrix[row][col] = ' '
            else:
                matrix[row][col] = 'x'
    return matrix

matrix = maze_maker(matrix)
pprint.pprint(matrix)


def move(matrix, pos):
    dir = input('what direction do you want to go')

    if dir == 'up':
        if self.pos_x > 0:
            self.pos_x = self.pos_x - 1
        return self.pos_x
