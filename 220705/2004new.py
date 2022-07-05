def cnt_two(n):
    two = 0
    while n!=0:
        if(n%2==0):
            n = n//2
            two += 1
        else:
            break

    return two

def cnt_five(n):
    five = 0
    while n!= 0:
        if(n%5==0):
            n = n//5
            five += 1
        else:
            break
    return five


A, B = map(int, input().split())

tot_two = cnt_two(A) + cnt_two(B)

tot_five = cnt_five(A) + cnt_five(B)


print(min(tot_two,tot_five))
