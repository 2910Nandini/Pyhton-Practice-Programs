#to separate operators and operand from a given operation string using list

x=input("enter an operation string")
l=len(x)
operand=" "
operator=" "
s=['+','-','*','/','%','^']
for i in range(l):
    if x[i] not in s:
        operand+=x[i]
    else:
        operator+=x[i]

print(operand)
print(operator)
