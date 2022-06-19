

prt = ['','','','','','','']
cnt=0

def CHK():
    global prt
    global n
    global cnt
    flag=0
    for i in range(n-2):
        if(prt[i]==prt[i+1] and prt[i]==prt[i+2]):
            flag=1
            #print(prt)
            break
        
    return flag


def REC(now,level):
    global prt
    global cnt
    if level==now:
        if CHK()==0:
            cnt +=1
            #print(prt)
        return
    
    for i in range(3):
        prt[now]=chr(int(ord('A'))+i)
        REC(now+1,level)


n = int(input())
REC(0,n)
print(cnt)
