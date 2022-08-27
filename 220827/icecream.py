
import sys
sys.stdin = open("icecreamin.txt","r")



def dfs(i,j):
    if arr[i][j]==1:
        return
    else:
        arr[i][j]=1
        if i+1 <N:
            dfs(i+1,j)
        if j+1 < M:
            dfs(i, j+1)
        if i-1 >=0:
            dfs(i-1, j)
        if j-1 >=0:
            dfs(i, j-1)





N,M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input())))
cnt=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            dfs(i,j)
            cnt+=1

print(cnt)

