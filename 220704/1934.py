import sys
sys.stdin = open("1934in.txt","r")



N = int(input())
for _ in range(N): 
    A, B = map(int, input().split())
    MN = min(A, B)
    GM = 1
    for i in range(MN, 1, -1):
        if(A % i == 0 and B % i == 0):
            GM = i
            break
    LM = A*B//GM
    print(LM)
