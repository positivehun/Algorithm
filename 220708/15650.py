N, M = map(int, input().split())
path = [0, 0, 0, 0, 0, 0, 0, 0]
DAT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def recur(level):
    global path
    global N
    global M
    if level == M:
        for i in range(M-1):
            if path[i] > path[i+1]:
                return
        for i in range(M):
            if path[i] != 0:
                print(path[i], end=' ')

        print()
        return
    for i in range(1, N+1):
        if DAT[i] == 1:
            continue
        path[level] = i
        DAT[i] = 1
        recur(level+1)
        path[level] = 0
        DAT[i] = 0


recur(0)
