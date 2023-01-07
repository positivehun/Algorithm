a = 1
b= a
print("a =",a,"b =",b)
a = 2
print("---a값을 2로 변경---")
print("a =",a,"b =",b)

c = [1,2,3,4,5]
d = c
print("c =",c)
print("c =",d)

print("c의 2번째 값을 9로 변경")
c[1] = 9
print("c =",c)
print("c =",d)

import copy

c = [1, 2, 3, 4]
d = copy.deepcopy(c)
d[1] = 0
print("------깊은 복사------")
print("c =",c)
print("d =",d)
