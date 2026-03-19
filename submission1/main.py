def calculate(a, b):
    result = []
    
    result.append(a + b)
    result.append(a - b)
    result.append(a * b)
    
    if b != 0:
        result.append(a / b)
    else:
        result.append("Division by zero")
    
    return result
