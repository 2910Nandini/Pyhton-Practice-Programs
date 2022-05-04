#to use set function 

a=[29,31,11,15,16,26,11,29,16]
print(type(a))
print(a)
a=set(a)
print(type(a))
print(a)
x=len(a)
print("length of set= ",x)
print("\nThe set elements are:-")
for i in a:
    print(i)
