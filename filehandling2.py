def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        for i in range(x,0,-1):
            y=y*i
        return y
user_input=15
y=fact(user_input)
print(user_input,y)

z="Factorial of "+str(user_input)+" is "+str(y)

f=open("sample.txt","a")
f.write(z)
f.write("---------------\n")
f.close()

f=open("sample.txt","r")
print(f.read())

