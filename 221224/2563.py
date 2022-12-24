import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221224/2563in.txt","r")

N = int(input())

MAP = [[0 for i in range(100)] for i in range(100)]

for k in range(N):
  x,y = map(int,input().split())
  for i in range(10):
    for j in range(10):
      MAP[x+i][y+j] = 1


cnt = 0
for i in range(100):
  for j in range(100):
    if MAP[i][j] ==1:
      cnt+=1
print(cnt)

