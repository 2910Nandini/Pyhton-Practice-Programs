operator = ["+","-","/","*","%"]
numeral = ["0","1","2","3","4","5","6","7","8","9","."]
expression = []
input_exp = input("Enter the value : ")
print("Input = " , input_exp)
operand = ""
for i in input_exp :
    if i in numeral :
        operand = operand+i
    elif i in operator :
        expression.append(operand)
        expression.append(i)
        operand = ""
    else :
        print("Invalid Character")
        break
expression.append(operand)
print("Input (in list) = ", expression )
