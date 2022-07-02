import sys
sys.stdin = open("11478in.txt","r")

n = input()
res = set()

for i in range(len(n)):
    for j in range(i,len(n)):
        t = n[i:j+1]
        res.add(t)


print(len(res))