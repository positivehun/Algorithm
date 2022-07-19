import sys
#sys.stdin = open("10773in.txt","r")
input = sys.stdin.readline

N = int(input())
lst=[]
for _ in range(N):
    A = int(input())
    if A == 0:
        lst.pop()
    else:
        lst.append(A)
print(sum(lst))