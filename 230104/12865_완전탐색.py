import sys
from itertools import combinations
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230104/12865in.txt","r")
input = sys.stdin.readline



N,K = map(int,input().split())
bag = [[0,0]]

for i in range(N):
  bag.append(list(map(int,input().split())))

index = []
for i in range(1,N+1):
  index.append(i)

answer = 0

for i in range(1,N+1):
  for k in list(combinations(index,i)):
    sum = 0 
    for t in k :
      sum += bag[t][0]
    if sum <= K: 
      weight=0
      for t in k :
          weight += bag[t][1]
      if answer < weight:
        answer = weight

print(answer)

