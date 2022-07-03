import sys
sys.stdin=open("3009in.txt","r")
X_con=[]
Y_con=[]
for i in range(3):
    A,B = map(int,input().split())
    X_con.append(A)
    Y_con.append(B)

for i in X_con:
    if X_con.count(i)==1:
        res_X = i
        break
for i in Y_con:
    if Y_con.count(i) == 1:
        res_Y = i
        break

print(res_X,res_Y)