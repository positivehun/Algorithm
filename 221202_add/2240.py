import sys
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221202_add/2240in.txt","r")
input = sys.stdin.readline

N,M = map(int,input().split())
cont = []
for i in range(N):
  cont.append(int(input()))
move=[]
con_count = []
now = 1
for i in range(N):
  if cont[i] != now:
    now = cont[i]
    move.append(i)

for i in range(1,len(move)):
  con_count.append(move[i]-move[i-1])
con_count.append(N-move[-1])

print(move)
print(con_count)

