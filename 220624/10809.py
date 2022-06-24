arr = list(input())
alpha=[-1]*26

for i in range(len(arr)):
    if alpha[ord(arr[i])-97] == -1:
        alpha[ord(arr[i])-97] = i

for i in alpha:
    print(i,end=' ')