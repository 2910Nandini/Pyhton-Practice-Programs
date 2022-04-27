#to print the table of a user defined integer

n=int(input("enter the no whose table is to be printed"))
m=n*10
x=1
for i in range(n,m+1,n):
    #print(n,"*",i//4,"=",i)  alternate method
    print("{}*{}={}".format(n,x,i))
    x=x+1
