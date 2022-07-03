import sys
sys.stdin = open("1002in.txt","r")

N =  int(input())
for _ in range(N):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dx = (x1-x2)**2
    dy = (y1-y2)**2
    rs = r1 + r2
    rm = abs(r1 - r2)
    d = (dx+dy)**0.5
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rs or d == rm:
            print(1)
        elif d < rs and d > rm:
            print(2)
        else:
            print(0)
