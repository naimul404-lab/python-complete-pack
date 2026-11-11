def calculate(a: float, operator: str, b: float) -> float:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b
    raise ValueError("unsupported operator")


def main() -> None:
    print("Simple calculator (+, -, *, /). Type q to quit.")
    while True:
        expression = input("Enter: ").strip()
        if expression.lower() == "q":
            break
        parts = expression.split()
        if len(parts) != 3:
            print("Use the format: number operator number")
            continue
        try:
            print(calculate(float(parts[0]), parts[1], float(parts[2])))
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
