import sys
sys.stdin = open("4344_in.txt","r")

n = int(input())
for i in range(n):
    scores = input().split()
    N = int(scores[0])
    cont = []
    for i in range(1,N+1):
        cont.append(int(scores[i]))
    avg = sum(cont)/len(cont)
    cnt=0
    for i in range(N):
        if (cont[i] > avg):
            cnt +=1
    per = cnt/N*100
    print('%.3f' % per + '%')

