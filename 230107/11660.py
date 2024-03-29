import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230107/11660in.txt","r")
input = sys.stdin.readline


n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
        
#print(dp)
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    answer = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)
