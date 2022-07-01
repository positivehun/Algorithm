
import sys
sys.stdin = open("11650in.txt","r")

n = int(input())
arr=[]
for i in range(n):
    arr.append([0,0])
for i in range(n):
    arr[i][0],arr[i][1] = map(int,sys.stdin.readline().split(' '))
   
arr.sort()
for i in range(n):
    print(arr[i][0],arr[i][1])