import sys
#sys.stdin = open("11021_in.txt","r")

n = int(input())
for i in range(1, n+1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #", end='')
    print(i, end='')
    print(":", end=' ')
    print(A,"+",B,"=",A+B)
