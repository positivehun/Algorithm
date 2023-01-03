import sys
from itertools import combinations
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230103/17070in.txt","r")
input = sys.stdin.readline

N = int(input())
MAP=[]
wall = []
answer=0
d = [[0,1],[1,0],[1,1]]
for _ in range(N):
  MAP.append(list(map(int,input().split())))

for i in range(N):
  for j in range(N):
    if MAP[i][j]==1:
      wall.append([i,j])


def dfs(i,j):
  global answer
  print(i,j)
  if i >= N or j >= N:
    return
  if i == N-1 and j == N-1:
    answer += 1
    return
  for k in wall:
    if k[0]==i and k[1]==j:
      return
    
  for k in d:
    dfs(i+k[0],j+k[1])
dfs(0,1)
print(answer)



