import sys
#sys.stdin = open("1149in.txt","r")

n = int(input())
MAP = []
for i in range(n):
    MAP.append(list(map(int, input().split())))
for i in range(1, len(MAP)):
    MAP[i][0] = min(MAP[i - 1][1], MAP[i - 1][2]) + MAP[i][0]
    MAP[i][1] = min(MAP[i - 1][0], MAP[i - 1][2]) + MAP[i][1]
    MAP[i][2] = min(MAP[i - 1][0], MAP[i - 1][1]) + MAP[i][2]
print(min(MAP[n - 1][0], MAP[n - 1][1], MAP[n - 1][2]))
