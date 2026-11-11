def greet(name: str, age: int = 18) -> str:
    return f"Hello {name}, you are {age} years old."


if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob", 25))
