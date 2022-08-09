import sys
#sys.stdin = open("2579in.txt","r")

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
if N > 2:
    dp=[]
    dp.append(arr[0])
    dp.append(max(arr[0]+arr[1],arr[1]))
    dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))

    for i in range(3,N):
        dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i]+arr[i-1]))

    print(dp[N-1])
elif N==2:
    print(max(arr[0]+arr[1],arr[1]))
elif N==1:
    print(arr[0])