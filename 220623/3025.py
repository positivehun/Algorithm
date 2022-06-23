#import sys
#sys.stdin = open("3025_in.txt","r")

cont=[]
re_cont=[0]*42
for i in range(10):
    cont.append(int(input())%42)

for i in range(10):
    re_cont[cont[i]] +=1
cnt=0
for i in range(42):
    if(re_cont[i]!=0):
        cnt +=1

print(cnt)

