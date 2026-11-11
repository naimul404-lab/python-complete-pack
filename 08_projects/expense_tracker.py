import json
from pathlib import Path

EXPENSES_FILE = Path("expenses.json")


def main() -> None:
    try:
        expenses = json.loads(EXPENSES_FILE.read_text(encoding="utf-8")) if EXPENSES_FILE.exists() else []
    except (OSError, json.JSONDecodeError):
        expenses = []

    while True:
        print("\n1. Add expense\n2. List and total\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            description = input("Description: ").strip()
            try:
                amount = float(input("Amount: "))
                if amount <= 0:
                    raise ValueError
            except ValueError:
                print("Enter a valid amount greater than zero.")
                continue
            expenses.append({"description": description, "amount": amount})
            EXPENSES_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")
        elif choice == "2":
            for item in expenses:
                print(f"{item['description']}: ${item['amount']:.2f}")
            print(f"Total: ${sum(item['amount'] for item in expenses):.2f}")
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
