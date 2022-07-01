import sys
sys.stdin = open("10814in.txt","r")

n = int(input())
arr=[]
for i in range(n):
    age,name = map(str,input().split())
    age = int(age)
    arr.append((age,name))

arr.sort(key=lambda arr: (arr[0]))

for i in range(n):
    print(arr[i][0],arr[i][1])
