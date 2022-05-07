#to implement arbitrary arguments

def avg(* value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=avg(5,95,30,78,31,29)
print(y)
