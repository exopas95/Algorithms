import sys


def paint(shape, row, col):
    if shape[row][col] == 2:
        return 0
    LEFT_UP = [max(0, row - 1), max(0, col - 1)]
    LEFT_BO = [min(len(shape) - 1, row + 1), min(col + 1, len(shape[0]) - 1)]
    RIGHT_UP = [min(len(shape) - 1, row + 1), min(col + 1, len(shape[0]) - 1)]
    RIGHT_BO = [max(0, row - 1), min(col + 1, len(shape[0]) - 1)]

    if col - LEFT_UP[1] == 1 and row - LEFT_UP[0] == 1:
        result = True
        for i in range(LEFT_UP[0], row + 1):
            for j in range(LEFT_UP[1], col + 1):
                if shape[i][j] == 0:
                    return False
        if result == True:
            for i in range(LEFT_UP[0], row + 1):
                for j in range(LEFT_UP[1], col + 1):
                    shape[i][j] = 2
            return 0
    
    if col - LEFT_BO[1] == 1 and row - LEFT_BO[0] == 1:
        result = True
        for i in range(LEFT_BO[0], row + 1):
            for j in range(LEFT_BO[1], col + 1):
                if shape[i][j] == 0:
                    return False
        if result == True:
            for i in range(LEFT_BO[0], row + 1):
                for j in range(LEFT_BO[1], col + 1):
                    shape[i][j] = 2
            return 0

    if col - RIGHT_UP[1] == 1 and row - RIGHT_UP[0] == 1:
        result = True
        for i in range(RIGHT_UP[0], row + 1):
            for j in range(RIGHT_UP[1], col + 1):
                if shape[i][j] == 0:
                    return False
        if result == True:
            for i in range(RIGHT_UP[0], row + 1):
                for j in range(RIGHT_UP[1], col + 1):
                    shape[i][j] = 2
            return 0

    if col - RIGHT_BO[1] == 1 and row - RIGHT_BO[0] == 1:
        result = True
        for i in range(RIGHT_BO[0], row + 1):
            for j in range(RIGHT_BO[1], col + 1):
                if shape[i][j] == 0:
                    return False
        if result == True:
            for i in range(RIGHT_BO[0], row + 1):
                for j in range(RIGHT_BO[1], col + 1):
                    shape[i][j] = 2
            return 0

row = []
shape = [[]]

tc = int(sys.stdin.readline())
for i in range(0, tc):
    shape.clear()

    N, M = list(map(int, sys.stdin.readline().split()))
    for j in range(0, N):
        row = list(map(int, sys.stdin.readline().split()))
        shape.append(row)
    
    for l in range(0, N):
        for m in range(0, M):
            paint(shape, l, m)
    result = True
    for n in range(0, len(shape)):
        for o in range(0, len(shape[n])):
            if shape[n][o] == 1:
                result = False
    if result:
        print("YES")
    else:
        print("NO")
	