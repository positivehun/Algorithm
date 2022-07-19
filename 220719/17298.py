from collections import deque
import sys
#sys.stdin = open("17298in.txt","r")
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = deque()
result = [-1]*N
for i in range(N):
    while stack:
        if lst[i] > lst[stack[-1]]:
            result[stack.pop()] = lst[i]
        else:
            break
    stack.append(i)

print(' '.join(map(str,result)))
