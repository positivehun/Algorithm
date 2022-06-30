import sys
sys.stdin = open("1018in.txt","r")
#n,m은 복사의 시작점
import copy
def Draw_B(arr_origin,n,m):
    cnt=0
    arr=[]
    for i in range(8):
        temp = copy.deepcopy(arr_origin[n+i][m:m+8])
        arr.append(temp)


    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0:
                if arr[i][j] != 'B':
                    cnt +=1
            elif i%2==1 and j%2==1:
                if arr[i][j] != 'B':
                    cnt +=1
            else:
                if arr[i][j] != 'W':
                    cnt+=1
    return cnt

def Draw_W(arr_origin,n,m):
    cnt=0
    arr=[]
    for i in range(8):
        temp = copy.deepcopy(arr_origin[n+i][m:m+8])
        arr.append(temp)
    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0:
                if arr[i][j] != 'W':
                    cnt +=1
                else:
                    continue
            elif i%2==1 and j%2==1:
                if arr[i][j] != 'W':
                    cnt +=1
            else:
                if arr[i][j] != 'B':
                    cnt+=1
    return cnt

n,m = map(int,input().split())
arr=[]
for i in range(n):
    k = input()
    arr.append(list(k))
#10,13
cnt_cont=[]
for i in range(n-7):
    for j in range(m-7):
        cnt_cont.append(Draw_B(arr, i, j))
        cnt_cont.append(Draw_W(arr, i, j))

print(min(cnt_cont))






