#infy 46

number=list(map(int,input().split()))
print(0,end=" ")
for i in range(1,len(number)):
    print(number[i-1]*2,end=" ")
    
____________________________________________________________________________________________________________
    
# infy 01

def add(str1):
  if(len(str1)>=3):
        if(str1.endswith("ing")):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
  
  return str1

str1="sleep"
print(add(str1))
_________________________________________________________________________________________________________________________

# infy 38

r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+','+str(j)
        n.append(temp)
    l.append(n)
print("[",end="")
print(*l,sep=',\n',end="")
print("]")
______________________________________________________________________________________________________________
#infy 3

import ast
def create_new_dictionary(prices):
    n=ast.literal_eval(prices)
    new_dict={}
    for key,value in n.items():
        if value> 200.0:
            new_dict[key]=value
    sorted_d= sorted(new_dict.items())
   
    return dict(sorted_d)
prices=input()
print(create_new_dictionary(prices))
______________________________________________________________________________________________________________
 # balanced brackets
    
    def valid(l,r):
    if(l=='(' and r==')'):
        return True 
    if(l=='[' and r==']'):
        return True
    if(l=='{'and r=='}'):
        return True 
    return False
def nest(s):
    stack=[] 
    for sym in s:
        if (sym == '[' or sym == '{' or sym == '('):
            stack.append(sym) 
        else:
            if len(stack)==0:
                return False
            last=stack.pop()
            if not valid(last,sym):
                return False
            
    if (len(stack)!=0):
        return False
    return True

N=int(input())
for i in range(N):
    s=input()
    if nest(s):
        print("YES")
    else:
        print("NO")

___________________________________________________________________________________________________
