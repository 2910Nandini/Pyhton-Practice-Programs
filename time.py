#to calculate the execution time of a program

from time import *

t1=time()
print("time before program run: ",t1)

n=int(input("enter number for factorial: "))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("factorial of {} is: {}".format(n,fact))

t2=time()
print("time after program run: ",t2)
