import sys
sys.stdin = open("PQ_1_in.txt","r")

from queue import PriorityQueue

que = PriorityQueue()


n = int(input())
arr=[]
for i in range(n):
    k = input()
    k = k.split(' ')
    arr.append(k)

for i in range(n):
    for j in range(i+1,n):
        if arr[i][j]== '0' or arr[i][j]=='-1':
            continue
        if int(arr[i][j])>0:
            que.put(int(arr[i][j]))

for i in range(10):
    temp = que.get()
    #print(temp,end=' ')
    temp = temp*2
    que.put(temp)
print(que.get()*2,end='')
print("만원")
    
