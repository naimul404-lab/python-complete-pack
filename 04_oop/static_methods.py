class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def square(value: float) -> float:
        return value * value


if __name__ == "__main__":
    print(MathUtils.add(2, 3))
    print(MathUtils.square(6))
