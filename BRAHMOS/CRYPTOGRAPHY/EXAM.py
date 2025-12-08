def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2
    elif op == '^':
        return n1 ** n2
    else:
        return "Invalid operator"


def main():
    print("Simple Python Calculator")
    while True:
        try:
            number1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, ^): ")
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
            continue

        result = calculate(number1, number2, operator)
        print(f"{number1} {operator} {number2} = {result}")

        cont = input("Continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()