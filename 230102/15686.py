import sys
from itertools import combinations
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230102/15686in.txt","r")
input = sys.stdin.readline

MAP=[]
chick = []
house = []
N,M = map(int,input().split())
dist = [[0 for _ in range(N)]for _ in range(N)]
for _ in range(N):
  MAP.append(list(map(int,input().split())))


for i in range(N):
  for j in range(N):
    if MAP[i][j]==2:
      chick.append([i,j])
    if MAP[i][j]==1:
      house.append([i,j])

min_dist = 99999999999

for arr in list(combinations(chick, M)):
  tot_temp = 0
  for h in house:
    temp = 999999
    for c in arr:
      dist_temp = abs(h[0]-c[0])+abs(h[1]-c[1])
      if dist_temp <temp :
        temp = dist_temp
    tot_temp += temp
  if tot_temp < min_dist:
    min_dist = tot_temp

print(min_dist)
    
    



