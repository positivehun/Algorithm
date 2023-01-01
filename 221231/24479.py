
import sys
input = sys.stdin.readline
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221231/24479in.txt","r")
sys.setrecursionlimit(10**8)

N,M,V = map(int,input().split())
graph = [[]for i in range(N+1)]
visit = [0]*(N+1)
cnt=1

for _ in range(M):
  i,j = map(int,input().split())
  graph[i].append(j)
  graph[j].append(i)
visit = [0]*(N+1)
def dfs(v):
  global cnt
  visit[v]=cnt
  graph[v].sort()
  for i in graph[v]:
    if visit[i]==0:
      cnt+=1
      dfs(i)

dfs(V)

for i in range(1,N+1):
  print(visit[i])


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())
# tree = [[] for _ in range(n+1)]
# par = [-1]*(n+1)
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# def dfs(n):
#     for i in tree[n]:
#         if par[i] == -1:
#             par[i] = n
#             dfs(i)
            
# dfs(1)
# for i in range(2,n+1):
#     print(par[i])


