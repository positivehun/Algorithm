import sys
sys.stdin = open("uglyin.txt","r")

N =  int(input())
arr = list(map(int,input().split()))


def ugly(n):
    re = 1
    n2, n3, n5 = [], [], []
    for i in range(n-1):
        n2 += [re*2]
        n3 += [re*3]
        n5 += [re*5]
        re = min(n2[0], n3[0], n5[0])
        if re == n2[0]:
            del n2[0]
        if re == n3[0]:
            del n3[0]
        if re == n5[0]:
            del n5[0]
        print(n2,n3,n5)
    return re

for i in arr:
    print(ugly(i),end=" ")