import math
A,B,V = map(int,input().split())

day = 0
V = V-A
day =math.ceil(V /(A-B))
day +=1



print(day)