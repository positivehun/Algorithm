
from queue import PriorityQueue
#import sys

#sys.stdin = open("10989_in.txt", "r")
que = PriorityQueue()


n = int(input())

for i in range(n):
    k = int(input())
    que.put(k)

for i in range(n):
    print(que.get())
