import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221202_add/5107in.txt","r")
input = sys.stdin.readline



def isChain(index,now):
  DAT[now]=1
  if cont[now][1]==cont[index][0]:
    ANSWER.append(index)
    return 
  for i in range(N):
    if DAT[i] == 0:
      if cont[now][1] ==  cont[i][0]:
        isChain(index,i)
        break
  return 0

case = 0
while (True):
  global ANSWER
  ANSWER = []
  case+=1
  N = int(input())
  if N == 0:
    break
  cont = []
  DAT = [0]*N
  for i in range(N):
    cont.append(list(input().split()))
  for i in range(N):
    isChain(i,i)


  print(case , len(ANSWER))



