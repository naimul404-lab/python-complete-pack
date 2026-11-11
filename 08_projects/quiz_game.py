QUESTIONS = [
    ("What is 2 + 2?", "4"),
    ("What is the keyword used to define a function in Python?", "def"),
    ("What data type represents True or False?", "bool"),
]


def main() -> None:
    score = 0
    for question, answer in QUESTIONS:
        if input(question + " ").strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Not quite—the answer is {answer}.")
    print(f"Final score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
