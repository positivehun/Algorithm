
import sys
#sys.stdin = open("11651in.txt","r")

n = int(input())
arr=[]
for i in range(n):
    arr.append([0,0])
for i in range(n):
    arr[i][1],arr[i][0] = map(int,sys.stdin.readline().split(' '))
   
arr.sort()
for i in range(n):
    print(arr[i][1],arr[i][0])