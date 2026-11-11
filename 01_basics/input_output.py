name = input("Enter your name: ").strip()
print(f"Hello, {name}!")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Age must be a whole number.")
else:
    print(f"You are {age} years old.")
