import sys
#sys.stdin = open("2675_in.txt","r")
sys.readline
n = int(input())

for i in range(n):
    A,B = input().split()
    B = list(B)
    for i in range(len(B)):
        print(B[i]*int(A),end='')
    print()
