import secrets
import string


def generate_password(length: int) -> str:
    if length < 1:
        raise ValueError("length must be at least 1")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    try:
        length = int(input("Password length: "))
        print(generate_password(length))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
