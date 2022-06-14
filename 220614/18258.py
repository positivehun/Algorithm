import sys
sys.stdin = open("input_18258.txt","r")

from collections import deque
queue = deque()
N = int(input())

for i in range(0,N):
    INPUT = input()
    INPUT = INPUT.split(" ")
    ORDER  = INPUT[0]
    if ORDER == "push":
        queue.append(INPUT[1])
    elif ORDER == "front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif ORDER == "pop":
        if len(queue) !=0:
            a = queue[0]
            queue.popleft()
        else:
            print(-1)
    elif ORDER == "size":
        print(len(queue))
    elif ORDER == "empty":
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif ORDER == "back":
        if(len(queue)!=0):
            print(queue[len(queue)-1])
        else:
            print(-1)