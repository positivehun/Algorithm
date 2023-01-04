import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230104/14494in.txt","r")
input = sys.stdin.readline

n,m = map(int,input().split())

MAP = [[0 for _ in range(n)]for _ in range(m)]

for i in range(n):
  MAP[0][i]=1
for j in range(m):
  MAP[j][0] = 1

for i in range(1,m):
  for j in range(1,n):
    MAP[i][j] = MAP[i-1][j] + MAP[i][j-1] + MAP[i-1][j-1]

print(MAP[-1][-1]%1000000007)
