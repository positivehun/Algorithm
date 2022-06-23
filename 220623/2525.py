H, M = map(int, input().split())
k = int(input())
M1 = k%60
H1 = k//60

H += H1
M += M1

if M>=60:
    H += 1
    M -= 60
if H >=24:
    H-=24

print(H,M)