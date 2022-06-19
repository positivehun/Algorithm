def PWD(PWD_IN):
    cnt = 0
    find_flag =0
    for i in range (65,91):
        if find_flag==1:
            break
        for j in range(65,91):
            if find_flag==1:

                break
            for k in range(65,91):
                if find_flag==1:
                    break
                for t in range(65,91):
                    cnt +=1
                    if (chr(i)+chr(j)+chr(k)+chr(t)==PWD_IN):
                        print(cnt)
                        find_flag=1
                        break
                        

n = int(input())

for i in range(n):
    pwd_in = input()
    PWD(pwd_in)