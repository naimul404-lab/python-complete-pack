class CountTo:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


if __name__ == "__main__":
    print(list(CountTo(5)))
