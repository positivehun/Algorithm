INF = 1000000000
N = 6
a = [[0,2,5,1,INF,INF],[2,0,3,2,INF,INF],[5,3,0,3,1,5],[1,2,3,0,1,INF],[INF,INF,1,1,0,2],[INF,INF,5,INF,2,0]]
v = [False]*N
d = [0]*N

def getSmallIndex():
    min = INF
    index=0
    for i in range(N):
        if d[i]<min and v[i]!=True:
            min=d[i]
            index = i
    return index


def dijkstra(start):
    for i in range(N):
        d[i] = a[start][i]
    v[start] = True
    for i in range(N-2):
        current = getSmallIndex()
        v[current] = True
        for j in range(N):
            if (v[j]!=True):
                if(d[current]+ a[current][j]<d[j]):
                    d[j] = d[current] + a[current][j]

def main():
    dijkstra(0)
    for i in range(N):
        print(d[i])
main()




