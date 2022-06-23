import sys
#sys.stdin = open("8958_in.txt","r")

n = int(input())
for i in range(n):
    k = list(input())
    score=0
    addit=0
    for j in range(len(k)):
        if k[j]=='O':
            addit +=1
            score += addit
            
        if k[j]=='X' :
            addit=0
    print(score)

