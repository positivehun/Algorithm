import sys
#sys.stdin = open("2751in.txt","r")

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(n):
    print(arr[i])
