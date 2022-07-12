import sys
#sys.stdin = open("1932in.txt","r")

N = int(input())
lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))

path=[]
dp=[]

def addp():
    cnt=lst[0][0]
    now=0
    for i in range(N-1):
        now+=path[i]
        cnt += lst[i+1][now]


    return cnt

def rec(level):
    if level==N-1:
        dp.append(addp())
        return
    for i in range(2):
        path.append(i)
        rec(level+1)
        path.pop()

rec(0)

print(max(dp))
