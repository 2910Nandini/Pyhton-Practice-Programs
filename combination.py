#to find the possible combinations for any two numbers

def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
    print("factorial of ",n,"=",fact_n)
    return(fact_n)

x=int(input("enter total "))
y=int(input("enter value "))

fx=fact(x)
fy=fact(y)
fxy=fact(x-y)

p=fx//(fy*fxy)
print("combination= ",p)
