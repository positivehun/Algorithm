import sys
sys.stdin = open("14888in.txt","r")
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
cal = list(map(int,input().split()))
path=[]
DAT=[0]*(N-1)


def calcul():
    result = int(arr[0])
    for i in range(N-1):
        if path[i]=='+':
            result += arr[i+1]
        elif path[i]=='-':
            result -= arr[i+1]
        elif path[i]=='*':
            result *= arr[i+1]
        elif path[i]=='/':
            result /= arr[i+1]
            result = int(result)
    
    return result
minn = 99999999
maxx = -99999999
def DFS(level):
    global maxx
    global minn
    if level == N-1:
        k = calcul()
        if maxx < k:
            maxx = k
        if minn > k:
            minn = k
        return
    for i in range(len(con)):
        if DAT[i]==0:
            DAT[i]=1
            path.append(con[i])
            DFS(level+1)
            path.pop()
            DAT[i]=0




pm = ['+','-','*','/']
con = []
for i in range(4):
    for _ in range(cal[i]):
        con.append(pm[i])

DFS(0)


print(maxx)
print(minn)