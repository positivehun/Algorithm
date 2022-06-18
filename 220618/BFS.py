arr = [[0,0,1,1,0,1],[0,0,0,1,1,1],[0,0,0,0,1,1],[0,0,0,0,0,0],[1,0,0,0,0,1],[0,0,0,0,0,0]]

visited = [0,0,0,0,0,0]

def BFS(level):
    visited[level]=1
    print(level,end=' ')
    for i in range(6):
        if arr[level][i]==0:
            continue
        if visited[i]==1:
            continue
        BFS(i)


n = int(input())     
BFS(n)