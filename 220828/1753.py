import sys
import heapq
sys.stdin = open("1753in.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e9)
N, M = map(int, input().split())
X = int(input())
distance = [INF]*(N+1)
graph = [[] for i in range(N+1)]

for _ in range(M):
    i, j, t = map(int, input().split())
    graph[i].append((j, t))
print(graph)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(X)

for i in range(1,N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

