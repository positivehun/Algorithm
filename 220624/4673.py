def SELNUM(number):
    if number < 100:
        return number + number%10 +number//10
    elif number < 1000 and number>=100:
        return number + number//100 + (number-number//100*100)//10 + number%10
    elif number < 10000 and number >=1000:
        return number + (number-number%1000)//1000 + ((number-number%100)%1000)//100 + ((number-number%10)%100)//10 + number%10


num_cont=[0]*12001
i=0
for i in range(10000):
    num_cont[SELNUM(i)] = 1
for i in range(10000):
    if(num_cont[i]==0):
        print(i)

