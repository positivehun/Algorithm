import sys
#sys.stdin = open("4949in.txt","r")
input = sys.stdin.readline

while(1):
    arr = list(input())
    if arr[0]=='.':
        break
    lst=[]
    for i in arr:
        if i == '(' or i == '[':
            lst.append(i)
        elif i == ')' :
            if len(lst) != 0 and lst[-1] == '(' :
                lst.pop()
            else:
                lst.append(i)
                break
        elif i == ']':
            if len(lst) != 0 and lst[-1] == '[':
                lst.pop()
            else:
                lst.append(i)
                break
    if len(lst)==0:
        print("yes")
    else:
        print("no")
    
  
        
    


