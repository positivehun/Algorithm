import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230108/16139in.txt","r")
input = sys.stdin.readline
DAT = [[] for _ in range(26)]
word = list(input())
for i in range(len(word)-1):
  DAT[ord(word[i])-97].append(i)
N = int(input())
for _ in range(N):
  alpha,start,end = map(str,input().split())
  start = int(start)
  end = int(end)
  answer=0
  for i in DAT[ord(alpha)-97]:
    if i >= start and i <= end:
      answer+=1
  print (answer)



