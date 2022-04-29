#to import a user defined module

import factorial2 as f

x=int(input("enter total no= "))
y=int(input("enter value= "))
fx=f.fact(x)
fy=f.fact(y)
fxy=f.fact(x-y)
p=fx//fxy
print("permutation= ",p)
c=fx//(fy*fxy)
print("combination= ",c)


            
