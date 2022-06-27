import sys
sys.stdin = open("2775in.txt","r")


def ban(k,n):
    f0 = [x for x in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            f0[j] += f0[j-1]
    return f0[-1]

n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())
    print(ban(k,n))


# 0층에 1 2 3 4 명
# 1층에 1 3 6 10명
# 2층에 1 4 10 20
# 3층에 1 5 15 35