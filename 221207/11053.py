import sys
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221207/11053in.txt","r")
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(N)]
for i in range(N):
  for j in range(i):
    if a[i]> a[j]  and dp[i]<dp[j]:
      dp[i] = dp[j]
      print(dp)
  dp[i] +=1

print(max(dp))



