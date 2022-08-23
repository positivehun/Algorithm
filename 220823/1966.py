import sys
sys.stdin = open("1966in.txt","r")

N = int(input())

for _ in range(N):
  A,B = map(int,input().split())
  arr = list(map(int,input().split()))
  print(A,B,arr)
