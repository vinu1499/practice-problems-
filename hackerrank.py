                                  test 1
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

____________________________________Test II__________________________________________________________
# infy 4
def find(num):
    for i in range(0,4):
        if(num[i]==9):
            return True
    return False
num=list(map(int,input().split()))
print(find(num))
_________________________________________________________________________________________________________
#infy 5
def countdigits(s):
    c=[]
    l1=0
    l2=0
    for i in s:
        if(i>="a" and i<="z"):
            l1+=1
        elif(i>="A" and i<="Z"):
            l1+=1
        elif(i>="0" and i<="9"):
            l2+=1
    c.append(l1)
    c.append(l2)
    return c
s=input()
print(countdigits(s))
_________________________________________________________________________________________________________
# infy 6
def check(l):
    for i in range(0,len(l)-1,1):
        if(l[i]==1 and l[i+1]==2 and l[i+2]==3):
            return True
    return False
        
             
l=list(map(int,input().split()))
print(check(l))
__________________________________________________________________________________________________________
# infy 29
def exchange(l):
    m=[]
    for i in range(len(l)-1,len(l)//2-1,-1):
        m.append(l[i])
    for i in range(0,len(l)//2):
        m.append(l[i])
    return m
l=list(map(int,input().split()))
print(*exchange(l))
____________________________________________________________________________________________________________________
# infy 31

def sum(l,n):
    a=len(l)
    r=0
    for i in range(1,a-1):
        if(l[i-1]!=n and l[i+1]!=n and l[i]!=n):
            r+=l[i]
    if(l[1]!=n and l[0]!=n):
        r+=l[0]
    if(l[a-2]!=n and l[a-1]!=n):
        r+=l[a-1]
    return r

l=list(map(int,input().split()))
n=int(input())
print(sum(l,n))
_________________________________________________________________________________________________________________________
