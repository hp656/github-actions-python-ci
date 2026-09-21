def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if(b == 0):
        raise ValueError("The divisor cannot be zero!") 
    return a / b