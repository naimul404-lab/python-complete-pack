def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
