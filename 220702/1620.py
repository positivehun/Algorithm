import sys
#sys.stdin = open("1620in.txt","r")
input =  sys.stdin.readline
N,M = map(int,input().split())
DIC = {}
for i in range(1,N+1):
    a = input().rstrip()
    DIC[i] = a
    DIC[a] = i

for i in range(M):
    k = input().rstrip()
    if k.isdigit():
        print(DIC[int(k)])
    else:
        print(DIC[k])
