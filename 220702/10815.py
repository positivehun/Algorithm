import sys
sys.stdin =open("10815in.txt","r")

HAVE_P = [0]*10000001
HAVE_M = [0]*10000001

N = int(input())
INPUT_N = input().split()
for i in INPUT_N:
    if int(i)>=0:
        HAVE_P[int(i)]=1
    elif int(i)<0:
        HAVE_M[-int(i)] = 1

M = int(input())
INPUT_M = input().split()
for i in INPUT_M:
    if int(i) >= 0:
        if HAVE_P[int(i)] == 1:
            print(1,end=' ')
        else:
            print(0,end=' ')
    elif int(i) < 0:
        if HAVE_M[-int(i)] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')

