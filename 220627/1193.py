n = int(input())

num=0
tot=0
while(True):
    tot += num
    if(n <= tot):
        break
    num +=1
#num은 고정
# 만약 num이 짝수라면 1/@부터시작
# num이 홀수라면 @/1부터 시작
se = num-tot+n
fi = num+1-se
if(num%2==0):
    temp = se
    se = fi
    fi = temp
print(str(fi)+"/"+str(se))