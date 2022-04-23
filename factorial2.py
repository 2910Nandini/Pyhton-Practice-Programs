#using recursion method

def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact(x-1)
        return y
n=int(input("Enter the number to calculate factorial:"))
factorial=fact(n)
print("factorial of {} is {}".format(n,factorial))
