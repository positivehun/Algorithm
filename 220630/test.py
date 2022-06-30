import copy
arr=[]
arr2 = [[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]]
temp = copy.deepcopy(arr2[1][0:3])
temp2 = copy.deepcopy(arr2[2][0:3])
arr.append(temp)
arr.append(temp2)
print(arr)