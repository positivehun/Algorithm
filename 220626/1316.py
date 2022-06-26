import sys
sys.stdin = open("1316in.txt","r")


def Group_check(k):
    DAT = [0]*26
    k = list(k)
    #97
    for i in range(len(k)):
        if(DAT[ord(k[i])-97]==0):   
            DAT[ord(k[i])-97] =1
        elif(DAT[ord(k[i])-97] == 1):
            if(k[i] == k[i-1]):
                continue
            else:
                return 1
                
    return 0

n = int(input())
cnt = n
for i in range(n):
    k = input()
    cnt -= Group_check(k)

print(cnt)

