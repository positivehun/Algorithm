import sys
#sys.stdin = open("1753in.txt","r")
sys.setrecursionlimit(10**4)
INF = int(1e9)
N,M = map(int,input().split())
X = int(input())

distance = [INF]*(N+1)
visited = [False]*(N+1)
graph = [[] for i in range(N+1)]

for _ in range(M):
    i,j,t = map(int,input().split())
    graph[i].append((j,t))




def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(X)

for i in range(1,N+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])