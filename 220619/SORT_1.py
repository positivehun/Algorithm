ref=[]
for i in range(5):
    k = input()
    k = list(k)
    ref.append(k)

n = input()
n = n.split(' ')
for i in range(2):
    ref[int(n[i])].sort()

for i in range(5):
    print(ref[i][0],end=' ')



