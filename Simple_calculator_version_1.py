print("="*50)
print ("                   Calculator                    ")
print("="*50)
number1 = int(input ("Please enter the first number : "))
number2 = int(input ("Please enter the second number : "))
operation_type = input("Please enter the operation that you want [+, -, *, /] ")
result = 0
if operation_type == '+':
    result = number1 + number2
elif operation_type == '-':
    result = number1 - number2
elif operation_type == '*':
    result = number1 * number2
else:
    result = number1 / number2
print (f"The operation result = {result}")
print("="*50)