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
arr = []
for i in range(N+1):
    if So(i) == 1:
        arr.append(i)
arr2 = []
while(True):
    for i in arr:
        if N % i == 0:
            arr2.append(i)
            N = N//i
    if(N == 1):
        break
arr2.sort()
for i in arr2:
    print(i)
