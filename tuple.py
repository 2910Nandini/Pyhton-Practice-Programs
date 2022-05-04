#to print a tuple before and after making changes

t1=(2,4,6,8,10)
t2=(1,3,5,7,9)
print("tuple 1= ",t1)
print("original location of tuple= ",id(t1))
print("tuple 2= ",t2)
t1+=t2
print("new tuple= ",t1)
print("new location of tuple= ",id(t1))
