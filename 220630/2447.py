
def STAR(n):
    if n==1:
        return ['*']
    Stars = STAR(n//3)
    L=[]
    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)
    
    return L

N = int(input())
print('\n'.join(STAR(N)))
