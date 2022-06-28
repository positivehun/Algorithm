def So(number):
    if number == 1:
        return 0
    else:
        cnt = 0
        for i in range(1, number+1):
            if number % i == 0:
                cnt += 1
        if cnt == 2:
            return 1
        else:
            return 0


N = int(input())
M = int(input())
arr=[]
for i in range(N,M+1):
    if So(i)==1:
        arr.append(i)

if(len(arr)==0):
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
