import sys
input = sys.stdin.readline


def check(x):
    for i in range(x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt

    if x == N:
        cnt += 1
        return

    for i in range(N):
        if DAT[i]:
            continue

        s[x] = i
        if check(x):
            DAT[i] = True
            dfs(x+1)
            DAT[i] = False


N = int(input())
s = [0] * N
DAT = [False] * N
cnt = 0

dfs(0)
print(cnt)
