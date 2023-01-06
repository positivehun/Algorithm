a = 1
b = a

print("a의 값의 주소 = ",id(a))
print("a의 변수의 주소 = ",id('a'))
print("b의 값의 주소 = ",id(b))
print("b의 변수의 주소 = ",id('b'))
print()
print("a를 2로 재할당 후")
a=2
print("a의 값의 주소 = ",id(a))
print("a의 변수의 주소 = ",id('a'))
print("b의 값의 주소 = ",id(b))
print("b의 변수의 주소 = ",id('b'))
arr = [1, 2, 3, ['a', 'b', 'c']]
print()
tuple = (1,2,3,4)
dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
dic2 = {1:100,2:200,3:300}
del dic2[1]
print(dic2)
print(list(tuple))
