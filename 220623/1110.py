n = int(input())
A = n//10
B = n % 10
cnt = 0
while(True):
    cnt +=1
    C = A+B
    New_n = B*10 + C%10
    if(New_n == n):
        print(cnt)
        break
    A = New_n//10
    B = New_n%10



