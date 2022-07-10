
import sys
input = sys.stdin.readline
sys.stdin = open("9184in.txt","r")

cache = {}
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    key = '{} {} {}'.format(a, b, c)

    if key in cache:
        return cache[key]
    res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    cache[key] = res

    return res


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
    