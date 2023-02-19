import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230219/2644in.txt","r")
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

def dfs(v, num):
  num += 1
  visited[v] = True

  if v == B:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

dfs(A, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)
