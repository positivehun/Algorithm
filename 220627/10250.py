import sys
sys.stdin = open("10250in.txt","r")
def ROOM(W,H,N):
    if(N/W == N//W):
        r_n = N//W
    else:
        r_n = (N//W)+1
    if(N%W==0):
        r_f = W
    else:
        r_f = N%W
    if(r_n<10):
        p_r_n = '0'+str(r_n)
    else:
        p_r_n=str(r_n)

    return int(str(r_f)+p_r_n)
n = int(input())
for i in range(n):
    W,H,N = map(int,input().split())
    k = ROOM(W,H,N)
    print(k)
