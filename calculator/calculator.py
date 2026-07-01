num1 = float(input("Enter the first number"))
operator = input("Enter the operator:('+','-','*','/','%')")
num2 = float(input("Enter the second number"))
match operator:
    case "+": # addition
        print(num1 + num2)
    case "-": # subtraction
        print(num1 - num2)
    case "*": # multiplication
        print(num1 * num2)
    case "/": # division
        print(num1 / num2)
    case "%": # modulus
        print(num1 % num2)
    case _:
        print("invalid operator")