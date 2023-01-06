import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230106/11054in.txt","r")
input = sys.stdin.readline




def lds(index,arr):
  dp = [1 for i in range(len(arr))]
  for i in range(index,len(arr)):
    s=[]
    for j in range(i):
      if arr[i] < arr[j]:
        s.append(dp[j])
    if not s:
      continue
    else:
      dp[i] += max(s)
  return max(dp)
def lis(index,arr):
  dp = [1 for _ in range(len(arr))]

  for i in range(index+1):
    for j in range(i):
      if arr[i] > arr[j]:
        dp[i] = max(dp[i],dp[j]+1)
  return max(dp)


N = int(input())
arr = list(map(int,input().split()))
max_idx=[]
max_val=0
for i in range(len(arr)):
  if arr[i] > max_val:
    max_val = arr[i]

for i in range(len(arr)):
  if arr[i] == max_val:
    max_idx.append(i)
answer=[]
for i in max_idx:
  answer.append(lds(i,arr)+lis(i,arr)-1)

print(max(answer))


