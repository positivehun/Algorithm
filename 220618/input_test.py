import sys
sys.stdin = open("input_DFS.txt","r")
list_k = []
a = int(input())
print(a)
for i in range(a):
    b = input()
    b = b.split()
    list_k.append(b)

print(list_k)
