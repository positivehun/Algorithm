import sys
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230219/14503in.txt","r")
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
MAP=[]
for i in range(N):
  MAP.append(list(map(int,input().split())))

print(MAP)
