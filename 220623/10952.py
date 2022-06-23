
import sys
sys.stdin = open("10952_in.txt","r")
while(True):
    A,B = map(int,input().split())
    if(A==B==0):
        break
    else:
        print(A+B)
