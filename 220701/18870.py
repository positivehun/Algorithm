import sys
#sys.stdin = open("18870in.txt","r")

n = int(input())
dic = {}
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(set(arr))
for i in range(len(arr2)):
    dic[arr2[i]] = i
for i in arr:
    print(dic[i],end=' ')


