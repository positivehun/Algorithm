import sys
sys.stdin = open("1037in.txt","r")
N = int(input())

arr = map(int,input().split())
print(max(arr)*min(arr))