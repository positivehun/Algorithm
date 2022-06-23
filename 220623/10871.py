import sys

#sys.stdin = open("10871_in.txt","r")
N,X = map(int,sys.stdin.readline().split())
arr = input().split()
for i in arr:
    if(int(i)<X):
        print(i,end=' ')