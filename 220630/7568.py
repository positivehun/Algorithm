import sys
sys.stdin = open("7568in.txt","r")

n = int(input())
H=[0]*n
W=[0]*n
for i in range(n):
    W[i],H[i] = map(int,input().split())

for i in range(n):
    rank=1
    for j in range(n):
        if(i==j):
            continue
        if W[i] < W[j] and H[i] < H[j]:
            rank +=1
    print(rank,end=' ')
    

