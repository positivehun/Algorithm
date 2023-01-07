import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230106/11054in.txt","r")
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp_i = [1 for _ in range(N)]
dp_d = [1 for _ in range(N)]

dp=[0]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_i[i] = max(dp_i[i], dp_i[j]+1)

arr.reverse()

for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp_d[i]=max(dp_d[i],dp_d[j]+1)
dp_d.reverse()
for i in range(N):
    dp[i]=dp_i[i]+dp_d[i]

print(max(dp)-1)

