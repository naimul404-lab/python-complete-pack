def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("division by zero is not allowed") from None


if __name__ == "__main__":
    try:
        print(divide(10, 0))
    except ValueError as error:
        print(f"Error: {error}")
