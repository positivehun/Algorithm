
import sys
#sys.stdin = open("2577_in.txt","r")
A = int(input())
B = int(input())
C = int(input())
N = A*B*C
N = list(str(N))
cont = [0]*10
for i in N:
    cont[int(i)] += 1

for i in range(10):
    print(cont[i]) 

