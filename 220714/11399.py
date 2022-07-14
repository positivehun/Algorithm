import sys
sys.stdin = open("11399in.txt","r")
N = int(input())
arr = list(map(int,input().split()))

arr.sort()
res=0
lst=[]
for i in arr:
    res+=i
    lst.append(res)
    

print(sum(lst))
