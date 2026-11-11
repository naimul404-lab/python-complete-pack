def countdown(start: int):
    while start > 0:
        yield start
        start -= 1


if __name__ == "__main__":
    print(list(countdown(5)))
