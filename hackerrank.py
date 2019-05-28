#infy 46
number=list(map(int,input().split()))
print(0,end=" ")
for i in range(1,len(number)):
    print(number[i-1]*2,end=" ")
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
