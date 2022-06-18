
import sys
sys.stdin = open("input_DFS.txt","r")
arr = []
n = int(input())
for i in range(n):
    b = input()
    b = b.split()
    arr.append(b)

def DFS(level):
    print(level,end=' ')
    for i in range(n):
        if arr[level][i]=='1':
            DFS(i)

DFS(0)
    