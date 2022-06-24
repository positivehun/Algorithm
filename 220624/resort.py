arr = list(input())
n = len(arr)
numcon=[]
strcon=[]

for i in range(n):
    if ord(arr[i])>=48 and ord(arr[i])<=57:
        numcon.append(arr[i])
    else:
        strcon.append(arr[i])

numcon.sort()
strcon.sort()

for i in strcon:
    print(i,end='')
hap=0
for i in numcon:
    hap+=int(i)
print(hap)
