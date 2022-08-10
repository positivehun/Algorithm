import sys
sys.stdin = open("mincodpin.txt","r")

arr=[]
for _ in range(4):
    arr.append(list(map(int,input().split(" "))))
print(arr)
