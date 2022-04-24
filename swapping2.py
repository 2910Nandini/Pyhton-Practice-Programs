print("This script is intended to swap values of two variables without using a third variable")
a=int(input())
b=int(input())
print("before swapping: a=",a," and b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping: a=",a," and b=",b)
