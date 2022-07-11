import sys
sys.stdin = open("1931in.txt","r")
lst=[]

N = int(input())
for _ in range(N):
    A,B = map(int,input().split())
    lst.append([A,B])
print(lst)


idx = -1
for i in range(N):
    if idx <lst[i][0]:
        



