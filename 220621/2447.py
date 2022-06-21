

arr = [[0 for i in range(9)] for i in range(9)]

print(arr)
for k in range(3):
    for t in range(3):
        if k == t == 1:
            continue
        for i in range(k*3,k*3+3):
            for j in range(t*3,t*3+3):
                if (i == k*3+1) and (j == t*3+1) :
                    continue
                arr[i][j]=1
for i in range(9):
    print(arr[i])
