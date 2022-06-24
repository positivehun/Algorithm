#arr = list(input())#
#arr = "aaaaaaa"
#arr = "aabbaccc"
arr = "abcabcabcabcdededededede"
#arr = "xababcdcdababcdcd"
temp_arr=[]

def MAKESMALL(unit):
    global arr
    global temp_arr
    temp_arr=[]

    for i in range(0,len(arr),unit):

        temp=''
        if i+unit <= len(arr):
            #print(i)
            for j in range(unit):
                temp = temp + arr[i+j]
            temp_arr.append(temp)
        else:
            for j in range(i,len(arr)):
                temp += arr[j]
            temp_arr.append(temp)


            

num_con=[0]*100
min_len=len(arr)
for i in range(1,len(arr)//2):
    num_con=[0]*100
    MAKESMALL(i)
    #print(temp_arr)
    idx=0
    cnt = 1
    for j in range(1,len(temp_arr)):
        if temp_arr[j] == temp_arr[j-1]:
            temp_arr[j-1]="#"
            cnt+=1
        elif temp_arr[j]!=temp_arr[j-1]:
            num_con[idx] = cnt
            idx +=1
            cnt=1
        if j == len(temp_arr)-1:
            num_con[idx] = cnt
            idx +=1
            cnt=1

    #print(temp_arr)
    len_idx=0
    result=""
    for i in range(len(temp_arr)):
        if temp_arr[i] == "#":
            continue
        else:

            result = result + str(num_con[len_idx]) + temp_arr[i]
            len_idx+=1
    result = list(result)
    new_result=[]
    for i in result:
        if i=='1':
            continue
        else:
            new_result.append(i)
    #print(len(new_result))
    if min_len>len(new_result):
        min_len = len(new_result)
print(min_len)



    




    

