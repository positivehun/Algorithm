A = int(input())
B = int(input())
B_1= B%10

B_10= (B%100-B_1)//10

B_100= (B-B_10-B_1)//100


print(A*B_1)
print(A*B_10)
print(A*B_100)
print(A*B)