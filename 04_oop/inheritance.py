class Animal:
    def speak(self) -> str:
        return "Animal sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


if __name__ == "__main__":
    for animal in (Dog(), Cat()):
        print(animal.speak())
