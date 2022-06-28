
import sys
sys.stdin = open("1978in.txt","r")

# 소수면 1 아니면 0
def So(number):
    if number == 1:
        return 0
    else:
        cnt=0
        for i in range(1,number+1):
            if number%i==0 :
                cnt+=1
        if cnt ==2:
            return 1
        else:
            return 0

n = int(input())
arr = input().split()
result = 0
for i in range(n):
    result += So(int(arr[i]))

print(result)

