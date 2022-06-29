import sys
sys.stdin = open("9020in.txt","r")

def So(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False 
    return True 

def DEV(number):
    T = number//2
    for i in range(T):
        if So(T-i):
            if(So(T+i)):
                print(T-i,T+i)
                break



N = int(input())

for i in range(N):
    K = int(input())
    DEV(K)
