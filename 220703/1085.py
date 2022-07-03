import sys
sys.stdin = open("1085in.txt","r")


x,y,w,h = map(int,input().split())
res = []
res.append(abs(x-0))
res.append(abs(x-w))
res.append(abs(y-0))
res.append(abs(y-h))

print(min(res))
