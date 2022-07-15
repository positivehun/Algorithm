import sys
sys.stdin = open("10828in.txt","r")
input = sys.stdin.readline

N = int(input())
lst=[]
for _ in range(N):
    A  = list(input().split())
    if (A[0]=="push"):
        lst.append(A[1])
    
    elif (A[0]=="pop"):
        if len(lst)==0:
            print(-1)
        else:
            print(lst[len(lst)-1])
            lst.pop()
    elif (A[0] == "size"):
        print(len(lst))
    elif (A[0] == "empty"):
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif (A[0] == "top"):
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[len(lst)-1])
    