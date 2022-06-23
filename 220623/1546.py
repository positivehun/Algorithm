
import sys
#sys.stdin = open("1546_in.txt","r")

n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

score_max = max(arr)

for i in range(n):
    arr[i] = arr[i]/score_max*100

avg = sum(arr)/len(arr)
print(avg)