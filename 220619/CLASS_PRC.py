class Calculator:
    def __init__(self):
        self.result = 0 # 기본적으로 저장되어있는 변수

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.result)
print(cal2.result)