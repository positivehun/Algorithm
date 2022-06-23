A,B,C = map(int, input().split())
if A==B==C:
    result = 10000 + A*1000
elif A==B!=C:
    result = 1000+100*A
elif A == C != B:
    result = 1000+100*A
elif C == B != A:
    result = 1000+100*B
else:
    result = max(A,B,C)*100

print(result)
