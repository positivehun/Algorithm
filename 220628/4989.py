import sys
sys.stdin = open("4989in.txt", "r")


def So(num):
    if num == 1:
        return 0
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return 0
        return 1
arr = [0]
for i in range(1,123456*2+1):
    if So(i):
        arr.append(1)
    else:
        arr.append(0)


while(True):
    N = int(input())
    if(N == 0):
        break
    result = arr[N+1:2*N+1]
    print(result.count(1))
    
