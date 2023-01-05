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
