#to check whether a number is even or odd

a=float(input("enter a number"))
print(type(a))
b=a%2
print(b)
print(int(b))
if(a==0):
        print("neither even nor odd")
elif(b==0):
        print("even")
else:
        print("odd")
