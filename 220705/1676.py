
N = int(input())

fact = 1
for i in range(1,N+1):
    fact*=i

fact = list(str(fact))
cnt=0
for i in range(len(fact)-1,-1,-1):
    if fact[i] == '0':
        cnt+=1
    else:
        print(cnt)
        break



