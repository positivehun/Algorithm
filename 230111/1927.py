import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230111/1927in.txt","r")
input = sys.stdin.readline
import heapq

N = int(input())

heap = []

for i in range(N):

  k = int(input())
  if k == 0:
    if len(heap)==0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
	  heapq.heappush(heap,k)

