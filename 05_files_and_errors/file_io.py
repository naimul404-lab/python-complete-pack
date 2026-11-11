from pathlib import Path

path = Path("sample.txt")
path.write_text("Hello, Python file I/O!\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"), end="")
