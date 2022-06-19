
def PWD(PWD_IN):
    PWD_IN=list(PWD_IN)
    cnt = (ord(PWD_IN[0])-ord('A'))*26*26*26+(ord(PWD_IN[1])-ord('A'))*26*26+(ord(PWD_IN[2])-ord('A'))*26+(ord(PWD_IN[3])-ord('A'))+1
    print(cnt)
n = int(input())

for i in range(n):
    pwd_in = input()
    PWD(pwd_in)