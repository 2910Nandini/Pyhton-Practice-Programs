#using index function in list

a=["nandu","silicon city",6263986055,"nandinijoshi/2016@gmail.com"]
print("list a= ",a)
print("NAME:- ",a[0])
print("ADDRESS:- ",a[1])
print("CONTACT:- ",a[2])
print("EMAIL:- ",a[3])

b=[1,2,3,4,5,6,7,8,9,10]
print("list b= ",b)
for i in range(len(b)):
    print(b[i])
x=int(input("enter index"))
y=b.index(x)
print("element at ",x,"index is ",y)
