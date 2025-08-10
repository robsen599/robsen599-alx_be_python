def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    a = 10
    b = 5
    print(f"Addition of {a} and {b} is {add(a, b)}")
    print(f"Subtraction of {a} and {b} is {subtract(a, b)}")
    print(f"Multiplication of {a} and {b} is {multiply(a, b)}")