import sys
sys.stdin = open("2981in.txt","r")

import math
N = int(input())

arr=[]

for _ in range(N):
    arr.append(int(input()))
arr.sort()

mog = arr[-1] - arr[0]
divisor = [mog]
for i in range(2, int(math.sqrt(mog)) + 1):
    if mog % i == 0:
        divisor.append(i)
        divisor.append(mog//i)

divisor = list(set(divisor))
divisor.sort()

for i in divisor:
    for j in range(N):
        if j == N - 1:
            print(i, end = " ")
        elif arr[j] % i != arr[j + 1] % i:
            break