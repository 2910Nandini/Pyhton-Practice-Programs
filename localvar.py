#local variable eg

def user_input():
    a=int(input("input 1st number"))
    b=int(input("input 2nd number"))
    return(a,b)

def add(a,b):
    return a+b

a,b=user_input()
c=add(a,b)
print(a,"+",b,"=",c)
