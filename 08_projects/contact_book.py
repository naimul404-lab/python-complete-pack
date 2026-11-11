import json
from pathlib import Path

CONTACTS_FILE = Path("contacts.json")


def load_contacts() -> dict[str, str]:
    if not CONTACTS_FILE.exists():
        return {}
    try:
        contacts = json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))
        return contacts if isinstance(contacts, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def main() -> None:
    contacts = load_contacts()
    while True:
        print("\n1. Add/update contact\n2. Search\n3. List\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts[name] = phone
                CONTACTS_FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")
        elif choice == "2":
            name = input("Name to find: ").strip()
            print(contacts.get(name, "Contact not found."))
        elif choice == "3":
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        elif choice == "4":
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
