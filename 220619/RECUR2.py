


def CHK():
    flag=0
    global prt

    for i in range(3):
        if(prt[i]=='B' and prt[i+1]=='T'):
            flag=1
            break
        elif(prt[i]=='T' and prt[i+1]=='B'):
            flag=1
            break
    return flag
def REC(now,level):
    global k
    global prt
    global cnt
    if now ==level:
        if CHK()==0:
            cnt+=1
        return
    for i in range(4):
        prt[now] = k[i]
        REC(now+1,level)


cnt=0
k = input()
k = list(k)

prt = ['' for i in range(10)]
REC(0,4)
print(cnt)
