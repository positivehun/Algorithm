
def DIS(num):
    arr = list(str(num))
    result = num
    for i in arr:
        result += int(i)

    return result


def GEN(num):
    arr = list(str(num))
    n = len(arr)
    if(num - n*9 > 0):
        for i in range(num - n*9,num):
            if DIS(i)==num:
                return i

        return 0
    else:
        for i in range(20):
            if DIS(i) == num:
                return i
        return 0


n = int(input())

print(GEN(n))
            




