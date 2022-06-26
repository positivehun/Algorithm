import sys
sys.stdin = open("1152in.txt","r")

n = input().split(' ')
cnt=0
for i in n:
    if i == '':
        cnt +=1
print(len(n)-cnt)