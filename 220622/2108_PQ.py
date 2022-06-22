from queue import PriorityQueue
import sys
sys.stdin = open("2108_in.txt","r")
DAT_P = [0]*4001
DAT_M = [0]*4001
que = PriorityQueue()
que1 = PriorityQueue()
n = int(input())
cont = []



for i in range(n):
    k=int(input())
    if(k>=0):
        DAT_P[k] +=1
    elif(k<0):
        DAT_M[abs(k)] +=1
    cont.append(k)

for i in cont:
    que.put(i)


#산술평균
avg = 0
que_max=-5000
que_min = 5000
for i in range(n):
    t = que.get()
    avg += t
    if(t > que_max):
        que_max = t
    if(t < que_min):
        que_min = t
avg = round(avg/n)
print(avg)

for i in cont:
    que1.put(i)
#중앙값
if n%2==0:
    for i in range(n/2):
        que1.get()
elif n % 2 == 1:
    for i in range(n//2):
        que1.get()
print(que1.get())

    
# #최빈값--> 맞지만 시간초과
maxx = 0
max_list=[]
for i in range(4001):
    if DAT_P[i]==0:
        continue
    if DAT_P[i]>maxx:
        maxx = DAT_P[i]
for i in range(4001):
    if DAT_M[i] == 0:
        continue
    if DAT_M[i] > maxx:
        maxx = DAT_M[i]
for i in range(4001):
    if (DAT_P[i]==maxx):
        max_list.append(i)
    if (DAT_M[i] == maxx):
        max_list.append(i*-1)

if len(max_list)==1:
    print(max_list[0])
else:
    que2 = PriorityQueue()
    for i in range(len(max_list)):
        que2.put(max_list[i])
    
    que2.get()
    print(que2.get())
# # 최빈값2


#범위
print(abs(que_max-que_min))


