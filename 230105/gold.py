import sys
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230105/goldin.txt","r")
input = sys.stdin.readline
def gold(n,m,arr):
  MAP = []
  GOLD = [[0 for i in range(m)]for i in range(n)]
  for i in range(n):
    MAP.append(arr[i*m:i*m+4])
  for i in range(n):
    GOLD[i][0] = MAP[i][0]
  
  for j in range(1,m):
    for i in range(n):
      if i == 0:
        GOLD[i][j] = max(GOLD[i][j-1]+MAP[i][j],GOLD[i+1][j-1]+MAP[i][j])
      elif i == n-1:
        GOLD[i][j] = max(GOLD[i-1][j-1]+MAP[i][j],GOLD[i][j-1]+MAP[i][j])
      else:
        GOLD[i][j] = max(GOLD[i-1][j-1]+MAP[i][j],GOLD[i][j-1]+MAP[i][j],GOLD[i+1][j-1]+MAP[i][j])
  answer=0
  for i in range(n):
    if GOLD[i][-1] >answer:
      answer = GOLD[i][-1]
  print(answer)
T = int(input())
for _ in range(T):
  N,M = map(int,input().split())
  ARR = list(map(int,input().split()))
  gold(N,M,ARR)
