import sys
sys.stdin = open("2981in.txt","r")


N = int(input())

arr=[]

for _ in range(N):
    arr.append(int(input()))


mx = max(arr)
for i in range(2,mx//2):
    flag=0
    temp = arr[0]%i
    for j in arr:
        if(temp == j%i):
            continue
        else:
            flag=1

    if flag==1:
        continue

    print(i,end=' ')