import sys
sys.stdin = open("input_1541.txt","r")
a = input()
a = list(a)
cont=[]
idx = 0
for i in range(len(a)):
    if a[i] == "-" or a[i] == "+":
        num_cont = ''
        for j in range(idx,i):
            num_cont = num_cont+a[j]
        cont.append(num_cont)
        cont.append(a[i])
        idx = i+1
num_cont = ''
for i in range(idx,len(a)):
    num_cont = num_cont+a[i]
cont.append(num_cont)

P_M = 0 # 0이면 더하기 1면 빼기
result = 0
for i  in range(len(cont)):
    if cont[i]!='-' and cont[i]!='+':
        if P_M==0:
            result  = result + int(cont[i])
        elif P_M == 1:
            result  = result - int(cont[i])
    elif cont[i]== "-":
        P_M = 1

    elif cont[i] == "+":

        P_M = 0
print(result)