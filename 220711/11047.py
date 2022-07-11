import sys
input = sys.stdin.readline
sys.stdin = open("11047in.txt","r")

N,K = map(int,input().split())
lst=[]
for _ in range(N):
    k = int(input())
    lst.append(k)

lst.reverse()
#print(lst)
cnt=0
for i in range(N):
    while(True):
        if lst[i] > K:
            break
        else:
            K -= lst[i]
            cnt+=1
print(cnt)





