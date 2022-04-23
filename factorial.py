#using iteration method

print("to find the factorial of a user defined number\n")
n=int(input())
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("factorial of {} is: {}".format(n,fact))








