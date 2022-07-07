N, M = map(int, input().split())

s = []


def recur(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        s.append(i)
        recur(i)
        s.pop()


recur(1)
