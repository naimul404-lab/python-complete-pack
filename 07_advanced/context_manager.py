from contextlib import contextmanager
from pathlib import Path


@contextmanager
def opened_text(path: str):
    file = Path(path).open("r", encoding="utf-8")
    try:
        yield file
    finally:
        file.close()


if __name__ == "__main__":
    sample = Path("sample.txt")
    sample.write_text("Context managers manage resources.\n", encoding="utf-8")
    with opened_text(str(sample)) as file:
        print(file.read(), end="")
