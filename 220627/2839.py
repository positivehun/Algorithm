N = int(input())
min_num = 5000
for i in range(1001):
    for j in range(1001):
        if(3*i+5*j == N):
            if(5*j>N):
                break
            if(min_num > i+j):
                min_num = i+j
if(min_num == 5000):
    min_num = -1
print(min_num)