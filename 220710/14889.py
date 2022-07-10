import sys
#sys.stdin = open("14889in.txt","r")
input = sys.stdin.readline

N = int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

path=[]
DAT = [0]*(N+1) 
gap = 999999999
def DIF():
    t_s=0
    t_l=0
    for i in range(N):
        for j in range(i+1,N):
            if DAT[i+1] == DAT[j+1]:
                if DAT[i+1] == 0:
                    t_s += arr[i][j]
                    t_s += arr[j][i]
                elif DAT[i+1] == 1:
                    t_l += arr[i][j]
                    t_l += arr[j][i]
    return t_s - t_l



def DFS(level):
    global gap
    if len(path) == N//2:
        g = abs(DIF())
        if g < gap:
            gap = g

        return
    for i in range(level,N+1):
        if DAT[i]==0:
            DAT[i]=1
            path.append(i)
            DFS(i)
            DAT[i]=0
            path.pop()

DFS(1)

print(gap)
