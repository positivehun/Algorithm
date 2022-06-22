
import sys
sys.stdin = open("2108_in.txt", "r")
from collections import Counter


t = int(sys.stdin.readline())

arr = []
for _ in range(t):
    arr.append(int(sys.stdin.readline()))

arr.sort()

#산술평균
def mean(nums):
    n =  len(nums)
    avg=0
    for i in arr:
        avg +=i
    avg = round(avg/n)
    return avg




#중앙값

def med(nums):
    n  = len(nums)
    return arr[n//2]

#최빈값


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()  # 1

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:  # 2
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]  # 3

    return mod


#범위
def scope(nums):
    n = len(nums)
    return abs(arr[0]-arr[n-1])


print(mean(arr))
print(med(arr))
print(mode(arr))  
print(scope(arr))

