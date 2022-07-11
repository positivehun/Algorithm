import sys
#sys.stdin = open("1931in.txt","r")
N = int(input())
lst = []

for _ in range(N):
  start, end = map(int, input().split())
  lst.append([start, end])

lst = sorted(lst, key=lambda a: a[0]) 
lst = sorted(lst, key=lambda a: a[1])

last = 0  
cnt = 0  

for i, j in lst:
  if i >= last:  
    cnt += 1
    last = j

print(cnt)
