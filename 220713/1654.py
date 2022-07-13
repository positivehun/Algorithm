import sys
#sys.stdin = open("1654in.txt","r")
#input = sys.stdin.readline


K, N = map(int,input().split())
con=[]
for _ in range(K):
    con.append(int(input()))

minn = min(con)
idx = sum(con)//N
for i in range(minn):
    result = 0
    k = idx - i
    for j in range(K):
       result +=  con[j]//k
    if result == N:
        print(k)
        break
