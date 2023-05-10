grid = [
    [1,5,0,0,3,0,6,2,9],
    [0,3,0,6,9,0,1,7,5],
    [0,0,0,0,0,0,4,8,0],
    [8,2,0,5,6,0,0,1,7],
    [0,0,7,3,8,1,0,4,0],
    [0,0,4,0,2,0,0,0,0],
    [7,9,1,8,0,6,0,0,4],
    [2,0,5,0,0,0,8,0,0],
    [6,0,0,9,0,2,0,0,1],
]

def solver(gd):

    find = find_empty(gd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(gd, i, (row, col)):
            gd[row][col] = i

            if solver(gd):
                return True

            gd[row][col] = 0

    return False
    


def is_valid(gd, num, pos):
    for i in range(len(gd[0])):
        if gd[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(gd[0])):
        if gd[i][pos[1]] == num and pos[0] != i:
            return False
        
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if gd[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(gd):
    for i in range(len(gd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(gd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(gd[i][j])
            else:
                print(str(gd[i][j]) + " ", end="")

def find_empty(gd):
    for i in range(len(gd)):
        for j in range(len(gd[0])):
            if gd[i][j] == 0:
                return (i, j)
    
    return None

print_board(grid)
solver(grid)
print("")
print_board(grid)