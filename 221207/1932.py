import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221207/1932in.txt","r")
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())))
dp = [[0 for i in range(n)]for i in range(n)] 
print(arr)
print(dp)
dp[0][0] = arr[0][0]
for i in range(n-1):
  for j in range(i+1):
    if dp[i+1][j] < dp[i][j] + arr[i+1][j]:
      dp[i+1][j]  = dp[i][j] + arr[i+1][j]
    if dp[i+1][j+1] < dp[i][j] + arr[i+1][j+1]:
      dp[i+1][j+1] = dp[i][j] + arr[i+1][j+1]

print(max(dp[n-1]))
