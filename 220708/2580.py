import sys
#sys.stdin = open("2580in.txt","r")
arr=[]
blank = []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

def checkRow(x,a):
    for i in range(9):
        if a == arr[x][i]:
            return False
    return True

def checkCol(y,a):
    for i in range(9):
        if a == arr[i][y]:
            return False
    return True

def checkBox(x,y,a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == arr[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkBox(x, y, i):
            arr[x][y] = i
            dfs(idx+1)
            arr[x][y] = 0


dfs(0)
