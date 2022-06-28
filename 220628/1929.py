def So(num):
    if num == 1:
        return 0
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return 0
        return 1


M, N = map(int, input().split())

for i in range(M, N+1):
    if So(i):
        print(i)
