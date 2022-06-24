#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
#  1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

def HAN(number):
    if number<100:
        return 1
    elif number<=1000 and number >=100:
        if ((number//100) -  (number-number//100*100)//10) == (number-number//100*100)//10-number%10 : 
            return 1
        else: 
            return 0


n = int(input())
cnt=0
for i in range(1,n+1):
    cnt += HAN(i)

print(cnt)
    
