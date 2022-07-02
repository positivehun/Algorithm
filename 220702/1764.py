
import sys
#sys.stdin = open("1764in.txt","r")
input = sys.stdin.readline

N,M = map(int,input().split())

H=[]
S=[]
for _ in range(N):
    t=  input().rstrip()
    H.append(t)

for _ in range(M):
    k = input().rstrip()
    S.append(k)

HS = list(set(H) & set(S))
HS.sort()
print(len(HS))
for i in HS:
    print(i)