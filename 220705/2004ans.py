A,B = map(int, input().split())


def two_cnt(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two


def five_cnt(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five


print(min(two_cnt(A) - two_cnt(A - B) - two_cnt(B),five_cnt(A) - five_cnt(A - B) - five_cnt(B)))
