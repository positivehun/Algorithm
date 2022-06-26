def Find_alpha(alpha):
    if (alpha in ['A','B','C']):
        return 3
    elif (alpha in ['D','E','F']):
        return 4
    elif (alpha in ['G', 'H', 'I']):
        return 5
    elif (alpha in ['J', 'K', 'L']):
        return 6
    elif (alpha in ['M', 'N', 'O']):
        return 7
    elif (alpha in ['P','Q','R','S']):
        return 8
    elif (alpha in ['T', 'U', 'V']):
        return 9
    elif (alpha in ['W','X','Y','Z']):
        return 10
    else:
        return 0

n = input()
n = list(n)
result=0
for i in n:
    result += Find_alpha(i)
    
print(result)

