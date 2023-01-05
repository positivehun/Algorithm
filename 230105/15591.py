import sys
from itertools import permutations
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230105/15591in.txt","r")
input = sys.stdin.readline

N,Q = map(int,input().split())
T = [[0 for _ in range(N+1)]for _ in range(N+1)]
USADO = []
Quest = []
temp=[]
for _ in range(N-1):
  USADO.append(list(map(int,input().split())))
for _ in range(Q):
  Quest.append(list(map(int,input().split())))


for i in USADO:
  T[i[0]][i[1]] = i[2]
  T[i[1]][i[0]] = i[2]



for i in range(1,N+1):
  for j in range(1,N+1):
    if i!=j and T[i][j]==0:
      ud = 0
      lr = 0
      ud_i=1
      lr_i=1
      ud_temp=[]
      lr_temp=[]
      while(True):
        if j+ud_i < N+1 and T[i][j+ud_i]!=0:
          ud_temp.append(T[i][j+ud_i])
        if j-ud_i > 0 and T[i][j-ud_i]!=0:
          ud_temp.append(T[i][j-ud_i])
        if len(ud_temp)==0:
          ud_i+=1
          continue
        elif(len(ud_temp)>0):
          ud = min(ud_temp)
          break

      while(True):
        if i+lr_i < N+1 and T[i+lr_i][j]!=0:
          lr_temp.append(T[i+lr_i][j])
        if i-lr_i > 0 and T[i-lr_i][j]!=0:
          lr_temp.append(T[i-lr_i][j])
        if len(lr_temp)==0:
          lr_i+=1
          continue
        elif(len(lr_temp)>0):
          lr = min(lr_temp)
          break
      temp.append([i,j,min(ud,lr)])
for i in temp:
  T[i[0]][i[1]]=i[2]
  T[i[1]][i[0]]=i[2]

for i in Quest:
  cnt=0
  for j in range(1,N+1):
    if(T[i[1]][j]>=i[0]):
      cnt+=1
  print(cnt)

