#using function method
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        for i in range(x,0,-1):
            y=y*i
        return y
funct_val=fact(5)
print("factorial of {} is {}".format(5,funct_val))
