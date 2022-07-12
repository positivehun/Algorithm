N = int(input())
lst=[]
for i in range(N):
    lst.append(int(input()))



MAX_NUM = max(lst)
arr = [1,1,1,2,2,3,4,5]
dp = [0]*(MAX_NUM+1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6,MAX_NUM+1):
    dp[i] = dp[i-1]+dp[i-5]

for i in range(N):
    print(dp[lst[i]])
