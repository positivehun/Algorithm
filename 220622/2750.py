import sys

sys.stdin = open("2750_in.txt","r")

from queue import PriorityQueue

que = PriorityQueue()

n = int(input())

for i in range(n):
    k=int(input())
    que.put(k)

for i in range(n):
    print(que.get())
    