import sys
sys.stdin = open("/Users/positive/Desktop/무제 폴더/Algorithm/221224/9251in.txt","r")

str1 = input()
str2 = input()

arr = [0 for i in range(len(str2))]

for i in range(len(str1)):
    max_num = 0
    for j in range(len(str2)):
        if max_num < arr[j]:
            max_num = arr[j]
        elif str1[i] == str2[j]:
            arr[j] = max_num + 1

print(max(arr))


