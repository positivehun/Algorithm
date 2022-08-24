
import sys
#sys.stdin = open("sweaA1in.txt","r")
import copy
path=[]
DAT=[0]*3

def movecnt1(path,EXIT):
    MAP =[0]*(L+1)
    temp = copy.deepcopy(EXIT)
    cnt = 0
    for i in path:
        idx = 0
        while(1):


            if i-idx >= 1 and MAP[i-idx]==0:
                MAP[i-idx] = 1
                temp[i]-=1
                cnt+=idx+1
                if temp[i]<=0:
                    break

            if i+idx <= L and MAP[i+idx]==0:
                MAP[i+idx] = 1
                temp[i]-=1
                cnt+=idx+1
                if temp[i] <= 0:
                    break
            
            idx+=1

    return cnt


def movecnt2(path, EXIT):
    MAP = [0]*(L+1)
    temp = copy.deepcopy(EXIT)
    cnt = 0
    for i in path:
        idx = 0
        while(1):
            if i+idx <= L and MAP[i+idx] == 0:
                MAP[i+idx] = 1
                temp[i] -= 1
                cnt += idx+1
                if temp[i] <= 0:
                    break
            if i-idx >= 1 and MAP[i-idx] == 0:
                MAP[i-idx] = 1
                temp[i] -= 1
                cnt += idx+1
                if temp[i] <= 0:
                    break

            idx += 1

    return cnt

                




def move(level,EXIT):
    if level==3:
        CON.append(movecnt1(path,EXIT))
        CON.append(movecnt2(path, EXIT))
        return

    for i in range(3):
        if DAT[i]==0:
            path.append(list(EXIT)[i])
            DAT[i]=1
            move(level+1,EXIT)
            path.pop()
            DAT[i]=0








def fish(L):
    EXIT = {}
    for _ in range(3):
        A,B = map(int,input().split())
        EXIT[A]=B
    move(0,EXIT)





def main():
    N = int(input())

    for t in range(N):
        global L
        global CON
        CON=[]
        L = int(input())
        fish(L)
        print("#"+str(t+1)+" "+str(min(CON)))

main()

