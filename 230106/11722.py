import sys
#sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/230106/11722in.txt","r")
input = sys.stdin.readline


N = int(input())

List = list(map(int, input().split()))

dp1 = [1]*N

sub_len=[0]*N

Max=0
List.reverse()
for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

print(max(dp1))
