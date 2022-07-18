import sys
sys.stdin = open("2559in.txt","r")

N,K = map(int,input().split())
arr = list(map(int,input().split()))
lst=[]
temp = sum(arr[:K])
lst.append(temp)
for i in range(N-K):
    temp -= arr[i]
    temp += arr[i+K]
    lst.append(temp)
    

print(max(lst))
