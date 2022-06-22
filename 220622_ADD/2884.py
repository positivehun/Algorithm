n = input().split()
H = int(n[0])
M = int(n[1])

if(M>=45):
    M = M-45
else:
    M = M+15
    if(H==0):
        H = 23
    else:
        H = H-1
print(H,M)
