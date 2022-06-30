n = int(input())
def tower(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        tower(n-1,a,c,b)
        print(a,c)
        tower(n-1,b,a,c)
cnt=0
for i in range(n):
    cnt = 2*cnt + 1
print(cnt)
tower(n,1,2,3)