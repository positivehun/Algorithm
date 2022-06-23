import sys
sys.stdin = open("10818_in.txt","r")
n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
print(min(arr),max(arr))
