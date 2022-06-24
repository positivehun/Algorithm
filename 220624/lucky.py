arr = list(input())
n = len(arr)
a1=0
a2=0
for i in range(0,n//2):
    a1 += int(arr[i])
for i in range(n//2,n):
    a2 += int(arr[i])

if(a1==a2):
    print("LUCKY")

else:
    print("READY")

