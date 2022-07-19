import sys
#sys.stdin = open("1874in.txt","r")
input = sys.stdin.readline

N = int(input())
lst1=[]
lst2=[]
result=[]
for i in range(N,0,-1):
    lst2.append(i)
lst1.append(lst2.pop())
result.append('+')
flag=0
for _ in range(N):
    k=int(input())
    while(1):
        if len(lst1)==0:
            flag=1
            break
        if lst1[-1]==k:
            result.append('-')
            lst1.pop()
            break
        else:
            lst1.append(lst2.pop())
            result.append('+')
    if flag==1:
        print('NO')
        break
if flag==0:
    for i in result:
        print(i)

