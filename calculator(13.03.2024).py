def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divers(x,y):
        if y==0:
            return "den mporw na dieresw me to 0"
        return x/y
def calculator():
    print('simple calculator')
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        
        

    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation.")
        return

    print(f"Result: {result}")
calculator()
    

    