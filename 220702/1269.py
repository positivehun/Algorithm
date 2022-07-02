import sys
#sys.stdin = open("1269in.txt","r")
input = sys.stdin.readline
N,M = map(int,input().split())
A = input().split()
B = input().split()

HAP = list(set(A) | set(B))
GYO = list(set(A) & set(B))
print(len(HAP)-len(GYO))
