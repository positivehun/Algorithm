A, B = map(int, input().split())

Mo = 1
Ja = 1
for i in range(B):
    Mo *= A
    A -= 1
for i in range(B):
    Ja *= B
    B -= 1

BI = Mo // Ja

BI = list(str(BI))
cnt = 0
for i in range(len(BI)-1, -1, -1):
    if BI[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break
