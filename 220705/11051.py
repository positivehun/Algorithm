A, B = map(int, input().split())

Mo = 1
Ja = 1
for i in range(B):
    Mo *= A
    A -= 1
for i in range(B):
    Ja *= B
    B -= 1

print((Mo // Ja)%10007)
