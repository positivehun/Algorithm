arr = list(input())
cont = [0]*26
for i in arr:
    if(ord(i)>=97 and ord(i)<=122):
        cont[ord(i)-97] +=1
    if(ord(i)>=65 and ord(i)<=90):
        cont[ord(i)-65] +=1

alpha_max = 0

for i in range(26):
    if cont[i]>alpha_max:
        alpha_max = cont[i]
result=[]
for i in range(26):
    if cont[i] == alpha_max:
        result.append(i)

if len(result)==1:
    print(chr(result[0]+65))
else:
    print("?")
