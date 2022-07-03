import sys
sys.stdin=open("2477in.txt","r")



Direction = []
Length = []
N = int(input())
for _  in range(6):
    D,L = map(int,input().split())
    Direction.append(D)
    Length.append(L)

MAP_SIZE=1
for i in range(6):
    if Direction.count(Direction[i]) == 1:
        MAP_SIZE *= Length[i]
        Length[i] = 0

MAP_MINUS=1
for i in range(6):
    if Length[i]==0:
        continue
    if Length[i-1]==0:
        continue
    if i < 5 and Length[i+1] == 0:
        continue
    if i == 5 and Length[0]==0:
        continue

    MAP_MINUS *= Length[i]

print((MAP_SIZE -MAP_MINUS)*N)









