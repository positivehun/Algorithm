import sys
sys.stdin = open("4153in.txt","r")

from queue import PriorityQueue
que = PriorityQueue()
while(1):
    A,B,C = map(int,input().split())
    if (A==0 and B==0 and C == 0):
        break
    que.put(A)
    que.put(B)
    que.put(C)
    chk = 0
    chk += que.get()**2
    chk += que.get()**2
    if chk == que.get()**2:
        print("right")
    else:
        print("wrong")