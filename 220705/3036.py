import sys
sys.stdin = open("3036in.txt","r")

import math
N = int(input())


arr = list(map(int,input().split()))

for i in range(1,N):
    gcd = math.gcd(arr[0], arr[i])
    print(arr[0]//gcd,end='')
    print('/',end='')
    print(arr[i]//gcd)
