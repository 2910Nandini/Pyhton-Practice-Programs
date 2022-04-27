print("to print divisors of a user defined number\n")
n=int(input())
print("divisors of {} are".format(n))
for i in range(1,n+1):
    if n%i==0:
        print(i)
