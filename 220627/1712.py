A,B,C = map(int,input().split())
cnt=1
if C-B <= 0:
        print(-1)
else:
    print(A//(C-B)+1)
