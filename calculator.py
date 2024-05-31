def main():
    print("Calculator Program")
    print("Input calculation, or x to exit")
    calculate = True
    while calculate:
        requested_calc = input()
        if requested_calc == "x":
            calculate = False
            break
        function = requested_function(requested_calc)
        print(calc(requested_calc, function))
        
        

def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1) / int(num2)

def requested_function(input):
    functions = ["+", "-", "*", "/"]
    for i in input:
        if i in functions:
            for func in functions:
                if func == i:
                    return func

def calc(calc, function):
    num1, num2 = calc.split(function)
    if function == "+":
        return add(num1, num2)
    if function == "-":
        return subtract(num1, num2)
    if function == "*":
        return multiply(num1, num2)
    if function == "/":
        return divide(num1, num2)

if __name__ == "__main__":
    main()