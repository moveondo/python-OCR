import random
import string
import sys

orig_stdout = sys.stdout
f = open('wordbank.txt', 'w')
sys.stdout = f

grid_size = 9
grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

def print_grid():
    for size in range(grid_size):
        print('\t'*2 + ''.join(grid[size]))

orientations = ['horizontal', 'vertical', 'diagonalup', 'diagonaldown']

f = open('wordbank.txt')
for word in f.read().split():
    word_length = len(word)

    placed = False
    while not placed:
        orientation = random.choice(orientations)

        if orientation == 'horizontal':
            step_x = 1
            step_y = 0
        if orientation == 'vertical':
            step_x = 0
            step_y = 1
        if orientation == 'diagonalup':
            step_x = 1
            step_y = 1
        if orientation == 'diagonaldown':
            step_x = 1
            step_y = -1

        x_position = random.randint(0,grid_size - 1)
        y_position = random.randint(0,grid_size - 1)

        ending_x = x_position + word_length * step_x
        ending_y = y_position + word_length * step_y

        if ending_x < 0 or ending_x >= grid_size: continue
        if ending_y < 0 or ending_y >= grid_size: continue

        failed = False

        for i in range(word_length):
            character = word[i]

            new_position_x = x_position + i * step_x
            new_position_y = y_position + i * step_y

            chcarcter_new_pos = grid[new_position_x][new_position_y]
            if chcarcter_new_pos != '_':
                if chcarcter_new_pos == character:
                    continue
                else:
                    failed = True
                    break
        if failed:
            continue
        else:
            for i in range(word_length):
                new_position_x = x_position + i * step_x
                new_position_y = y_position + i * step_y
                grid[new_position_x][new_position_y] = word[i]
            placed = True

for x in range(grid_size):
    for y in range(grid_size):
        if grid[x][y] == '_':
            grid[x][y] = random.choice(string.ascii_uppercase)

print_grid()

sys.stdout = orig_stdout
f.close()
