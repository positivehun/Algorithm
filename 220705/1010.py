import sys
sys.stdin = open("1010in.txt","r")

N = int(input())
for _ in range(N):

    A, B = map(int, input().split())
    Ja=1
    Mo=1
    for _ in range(A):
        Ja *= B
        B -= 1
    for _ in range(A):
        Mo *= A
        A -= 1
    print(Ja // Mo)
