import sys
from itertools import permutations
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230105/18429in.txt","r")
input = sys.stdin.readline


N,K = map(int,input().split())
kit = list(map(int,input().split()))
index = []
for i in range(N):
  index.append(i+1)

answer=0
for i in list(permutations(index)):
  flag=0
  sum = 0
  for j in i:
    sum -= K
    sum += kit[j-1]
    if sum < 0:
      flag=1
      break
  if flag == 0:
    answer +=1

print(answer)


