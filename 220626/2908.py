import sys
sys.stdin = open("2908in.txt","r")

def REVER(number):
    number = list(str(number))
    temp=''
    for i in range(len(number)-1,-1,-1):
        temp += number[i]
    return int(temp)

A,B = map(int,input().split())
A = REVER(A)
B = REVER(B)
print(max(A,B))
