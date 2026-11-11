students: list[dict[str, str]] = []


def main() -> None:
    while True:
        print("\n1. Add student\n2. List students\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            grade = input("Grade: ").strip()
            if name and grade:
                students.append({"name": name, "grade": grade})
        elif choice == "2":
            for student in students:
                print(f"{student['name']}: {student['grade']}")
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
