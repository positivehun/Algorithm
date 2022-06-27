import sys
sys.stdin = open("10757in.txt","r")

A,B = input().split()
result = []
A = list(A)
B = list(B)
A.reverse()
B.reverse()
NA = len(A)
NB = len(B)
max_len = 0
if(NA == NB):
   max_len = NA
elif max(NA,NB)==NA:
    for i in range(abs(NA-NB)):
        B.append('0')
    max_len = NA
elif max(NA,NB)==NB:
    for i in range(abs(NA-NB)):
        A.append('0')
    max_len = NB
next=0
for i in range(max_len):
    num = int(A[i])+int(B[i])+next
    if(num>=10):
        next = 1
    else:
        next=0
    
    num = num%10
    result.append(num)

if (next == 1):
    result.append(1)

result.reverse()
for i in result:
    print(i,end='')
