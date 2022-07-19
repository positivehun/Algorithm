
import sys
#sys.stdin = open("1874in.txt","r")
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
result = []
flag = 1

for i in range(0, n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        flag = 0
        break

if flag == 0:
    print("NO")
else:
    print("\n".join(result))
