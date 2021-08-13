def inc(x, y):
    return x + y

def decr(x, y):
    return x - y

def mult(x, y):
    return x * y

def divide(x, y):
    return x / y

def execute(num1, num2, operator):
    # maybe add a switch statement
    if operator == "+":
        return inc(num1, num2)
    elif operator == "-":
        return decr(num1, num2)
    elif operator == "*":
        return mult(num1, num2)
    elif operator == "/":
        return divide(num1, num2)