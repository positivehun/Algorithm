
temp_arr=[]

def MAKESMALL(unit):
    global arr
    global temp_arr
    temp_arr=[]

    for i in range(0,len(arr),unit):

        temp=''
        if i+unit <= len(arr):
            for j in range(unit):
                temp = temp + arr[i+j]
            temp_arr.append(temp)
        else:
            for j in range(i,len(arr)):
                temp += arr[j]
            temp_arr.append(temp)

def solution(s):
    global arr
    arr = list(s)
    num_con=[0]*1001
    min_len=len(arr)
    for i in range(1,len(arr)//2+1):
        num_con=[0]*1001
        MAKESMALL(i)

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


        len_idx=0
        result=""
        for i in range(len(temp_arr)):
            if temp_arr[i] == "#":
                continue
            else:

                result = result + str(num_con[len_idx]) + temp_arr[i]
                len_idx+=1
        print(result)
        result = list(result)

        new_result=[]
        for i in result:
            if i=='1':
                continue
            #if i=='0':
                #continue
            else:
                new_result.append(i)

        if min_len>len(new_result):
            min_len = len(new_result)
    answer=min_len
    return answer


print(solution("aabbaccc"))