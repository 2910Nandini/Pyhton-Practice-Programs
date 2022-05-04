def addition(a,b):
    sum=0
    sum=a+b
    return(sum)

def subtraction(a,b):
    diff=0
    diff=a-b
    return(diff)

def multiplication(a,b):
    mult=1
    mult=a*b
    return(mult)

def division(a,b):
    div=1
    div=a/b
    return(div)

def modulus(a,b):
    mod=a%b
    return(mod)

def square(a):
    sq=a*a
    return(sq)

def cube(a):
    cb=a*a*a
    return(cb)

def power(a,b):
    powe=a**b
    return(powe)

def sqroot(a):
    sqrt=a**(1/2)
    return(sqrt)

def cbroot(a):
    cbrt=a**(1/3)
    return(cbrt)

def bvalue():
    b2=int(input("re-enter the second number"))
    operation()
    
def operation():
    op=int(input("enter operation to be performed:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n7.Square\n8.Cube\n9.Square root\n10.Cube root\n"))

    if op==1:                     #for addition
        a,b = doubleinput()
        add=addition(a,b)
        print(a,"+",b,"= ",add)
    elif op==2:                        #for subtraction
        a,b = doubleinput()
        sub=subtraction(a,b)
        print(a,"-",b,"= ",sub)
    elif op==3:                     #for multiplication
        a,b = doubleinput()
        prod=multiplication(a,b)
        print(a,"*",b,"= ",prod)
    elif op==4:                      #for division
        a,b = doubleinput()
        if b==0:
            print("zero division error")
            bvalue()
        else:
            divi=division(a,b)
            print(a,"/",b,"= ",divi)
    elif op==5:                         #for modulus
        a,b = doubleinput()
        if b==0:
            print("zero division error")
            bvalue()
        else:
            modu=modulus(a,b)
            print(a,"%",b,"= ",modu)
    elif op==6:                                 #for calculating power
        a,b = doubleinput()
        powe=power(a,b)
        print(a," to the power ",b,"= ",powe)
    elif op==7:                               #to find square
        a=singleinput()
        sq=square(a)
        print(a," square is ",sq)
    elif op==8:                             #to find cube
        a=singleinput()
        cb=cube(a)
        print(a," cube is ",cb)
    elif op==9:                                #to find square root
        a=singleinput()
        sqrt=sqroot(a)
        print("square root of ",a,"is ",sqrt)
    elif op==10:                              #to find cube root
        a=singleinput()
        cbrt=cbroot(a)
        print("cube root of ",a,"is ",cbrt)
    else:
        print("invalid operator")

    ch=input("Do you want to Continue?..\nEnter 'Y' for YES\nEnter 'N' for NO\n")
    if ch=='Y':
        operation()
    elif ch=='N':
        print("THANK YOU for using my calculator...!!!")
    else:
        print("invalid entry")

def doubleinput():                 #to input two numbers
    num=int(input("which type of numbers do you want to enter\n1.integer\n2.float\n"))

    if num==1:
        a,b=int(input("enter both integers")),int(input())
    elif num==2:
        a,b=float(input("enter both float numbers")),float(input())
    else:
        print("invalid choice")
        exit()
    return a,b

def singleinput():                 #to input one single number
    num=int(input("which type of number do you want to enter\n1.integer\n2.float\n"))

    if num==1:
        a=int(input("enter the number"))
    elif num==2:
        a=float(input("enter the number"))
    else:
        print("invalid choice")
        exit()
    return a

#main program
print("WELCOME!! To NANDINI'S CALCULATOR\n")
operation()

