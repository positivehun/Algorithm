import sys
#sys.stdin = open("10989in.txt","r")

n = int(input())
arr = [0]*10001
for i in range(n):
    arr[int(sys.stdin.readline())] +=1

for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)
