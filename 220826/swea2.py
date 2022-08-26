import sys
sys.stdin = open("swea2in.txt","r")

path = []
DAT = [0]*10




def movecnt(path):
    cnt = 0
    now_i=0
    now_j=0
    for i in range(len(path)):
        for j in range(len(loc)):
            if path[i] == loc[j][0]:
                cnt += abs(now_i - loc[j][1])
                now_i = loc[j][1]
                cnt += abs(now_j - loc[j][2])
                now_j = loc[j][2]
    return cnt








def isValid(path):
    lst = [0,0,0,0,0]
    for i in range(len(path)):
        if path[i] >=0:
            lst[path[i]]=1
        else:
            if lst[path[i]*-1]!=1:
                return 0
            else:
                continue
    return 1
        



def dfs(level):
    if level == len(cont):
        if(isValid(path)==1):
            result.append(movecnt(path))
        return
    for i in range(len(cont)):
        if DAT[i]==0:
            path.append(cont[i])
            DAT[i]=1
            dfs(level+1)
            path.pop()
            DAT[i]=0




def hunt():
    global cont
    global loc
    loc = []
    cont = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] !=0:
                cont.append(MAP[i][j])
                loc.append([MAP[i][j],i,j])
                
    dfs(0)









def monster():
    global result
    global N
    global MAP
    result=[]
    N =  int(input())
    MAP=[]
    for _ in range(N):
        MAP.append(list(map(int,input().split())))
    hunt()

    





def main():
    N = int(input())
    T=1
    for _ in range(N):
        monster()
        print('#%d %d'%(T,min(result)))
        T+=1

main()