from queue import PriorityQueue

que = PriorityQueue()

arr = [1,5,4,2,-5,-7]
for i in arr:
    que.put(i)


n = int(input())
k = 6-n
for i in range(k):
    que.get()
    3
print(que.get())

