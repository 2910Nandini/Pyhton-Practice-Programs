#lambda or anonymous fucntion 

from functools import reduce

list1 = [2,13,42,4,524,331,452,321,22]

list_even = list(filter(lambda x : x%2==0,list1))
list_odd = list(filter(lambda x : x%2!=0,list1))

list_even2 = list(map(lambda x : x*2,list_even))

sum = reduce(lambda x,y : x+y, list_even2)

print("list1= ",list1)
print("even list= ",list_even)
print(type(list_even))
print("odd list= ",list_odd)
print("multiplying each element of even list by 2= ",list_even2)
print("sum of elements of the list= ",sum)
