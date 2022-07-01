n = input()
n = list(n)
n.sort()
for i in range(len(n)-1,-1,-1):
    print(n[i],end='')