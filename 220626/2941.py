def Cro_alpha(alpha):
    alpha = list(alpha)
    cnt = len(alpha)
    for i in range(len(alpha)):
        if (alpha[i]=='='):
            if(alpha[i-1] in ['c','s']):
                cnt -= 1
            elif(alpha[i-1]=='z'):
                cnt -=1
                if(alpha[i-2] == 'd'):
                    cnt-=1
        elif (alpha[i]=='-'):
            if(alpha[i-1]in ['c','d']):
                cnt-=1
        elif(alpha[i]=='j'):
            if(alpha[i-1]in['l','n']):
                cnt-=1
    
    return cnt

n = input()
print(Cro_alpha(n))