N = int(input())

arr = [0]
arr.append(9)

for i in range(1,N):
    arr.append((arr[i]-i)*2+i)

print(arr[N] % 1000000000)

