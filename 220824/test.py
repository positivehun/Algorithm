a = {}
path = []
a[3]=5
a[2]=100
print(list(a)[1])
print(a[list(a)[1]])
path.append(list(a)[1])
path.append(list(a)[0])
print(path)
print(a[path[0]])
a[path[0]] -=1
print(a[path[0]])
