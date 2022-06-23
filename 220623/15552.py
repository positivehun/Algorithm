import sys
#sys.stdin = open("15552_input.txt","r")

n = int(input())
for i in range(n):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)

# 맨 첫줄 Test case를 입력받을 때는 input()을 사용해도 무방합니다.
#그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.
