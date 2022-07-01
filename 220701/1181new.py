import sys
sys.stdin = open("1181in.txt","r")

n = int(input())
arr=[]
temp=''
for i in range(n):
    
    k = sys.stdin.readline()
    if k in arr:
        continue
    else:
        arr.append(k)
        temp = k 
print(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if len(arr[i]) > len(arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        elif len(arr[i]) == len(arr[j]):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

for i in range(len(arr)):
    print(arr[i])
