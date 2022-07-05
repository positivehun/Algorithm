import sys
sys.stdin = open("9375in.txt","r")

N =  int(input())
arr=[]
CATE = []
for _  in range(N):
    arr.clear()
    CATE.clear()
    M = int(input())
    for _ in range(M):
        CL,CA = input().split()
        if CA not in CATE:
            CATE.append(CA)
            arr.append(1)
        else:
            for i in range(len(CATE)):
                if CA == CATE[i]:
                    arr[i]+=1
    res=1
    for i in arr:
        res *= i+1
    print(res-1)

        