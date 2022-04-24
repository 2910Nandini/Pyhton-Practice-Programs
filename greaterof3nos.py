#to find the greatest of three integers which are user defined

a,b,c=int(input("enter three numbers")),int(input()),int(input())
if a==b==c:
    print("all three nos are equal")
elif a==b and a>c:
    print(a,"and",b,"are equal and greater than",c)
elif b==c and b>a:
    print(b,"and",c,"are equal and greater than",a)
elif a==c and a>b:
    print(a,"and",c,"are equal and greater than",b)
elif a==b and a<c:
    print(a,"and",b,"are equal and less than",c)
elif b==c and b<a:
    print(b,"and",c,"are equal and less than",a)
elif a==c and a<b:
    print(a,"and",c,"are equal and less than",b)
elif a>b and a>c:
    print(a,"is greater than",b,"and",c)
elif b>a and b>c:
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)
