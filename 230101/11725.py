import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230101/11725in.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
#arr = [[0 for _ in range(N+1)]for _ in range(N+1)]
arr_i = []
arr_j = []
visited = [0 for _ in range(N+1)]
for _ in range(N-1):
  i,j = map(int,input().split())
  arr_i.append(i)
  arr_j.append(j)

def dfs(par,node):
  visited[node] = par
  for i in range(N-1):
    if arr_j[i]==par:
      continue
    if arr_i[i]==node and visited[arr_j[i]]==0:
      dfs(node,arr_j[i])
  for i in range(N-1):
    if arr_i[i]==par:
      continue
    if arr_j[i]==node and visited[arr_i[i]]==0:
      dfs(node,arr_i[i])


dfs(0,1)

for i in range(2,N+1):
  print(visited[i])
