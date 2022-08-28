import sys
from queue import PriorityQueue
sys.stdin = open("uglyin.txt","r")

N = int(input())
arr = list(map(int, input().split()))
q = PriorityQueue()
q.put(1)
cnt=0
old=-1
result = [0 for i in range(20)]
while(1):
    now = q.get()
    if(old ==now): continue
    old = now
    cnt+=1
    result[cnt] = now
    if(cnt==1500):break

    q.put(now*2)
    q.put(now*3)
    q.put(now*5)
    print(now)


for i in arr:
    print(result[i],end=" ")

