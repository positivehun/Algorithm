import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221229/2565in.txt","r")
n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))




