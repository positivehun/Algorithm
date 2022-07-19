import sys
#sys.stdin = open("9012in.txt","r")
input = sys.stdin.readline

N = int(input())
for _  in range(N):
    arr = list(input())
    result=0
    flag=0
    for i in arr:
        if i=='(':
            flag +=1
        elif i==')':
            flag -=1
        
        if flag==-1:
            result=1
            break
    if flag == 0 and result==0:
        print("YES")
    else:
        print("NO")
    

