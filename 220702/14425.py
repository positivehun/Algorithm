import sys
sys.stdin = open("14425in.txt","r")

N,M = map(int,input().split())
S = []
CHECK = []
for i in range(N):
    S.append(input())

for i in range(M):
    CHECK.append(input())

cnt=0
for i in CHECK:
    if i in S:
        cnt+=1
print(cnt)

