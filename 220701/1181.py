import sys
sys.stdin = open("1181in.txt","r")
n = int(input())
arr=[]
for i in range(n):
    arr.append([''])
for i in range(n):
    arr[i].append(list(sys.stdin.readline()))
   
for i in range(n):
    for j in range(i+1,n):
        if len(arr[i][1]) > len(arr[j][1]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
temp1=''
for i in range(n):
    result = ''
    for j in range(len(arr[i][1])):
        result += arr[i][1][j]

    if(temp1 == result ):
        continue
    else:
        print(result)
        temp1 = result
