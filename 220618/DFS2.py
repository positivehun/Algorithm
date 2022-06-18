import sys
sys.stdin = open("input_DFS2.txt","r")

STR_CONT = input()
STR_CONT = list(STR_CONT)

arr = []
for i in range(8):
    b = input()
    b = b.split()
    arr.append(b)

def DFS(level):
    print(STR_CONT[level],end='')
    for i in range(8):
        if arr[level][i]=='1':
            DFS(i)

DFS(0)

    
