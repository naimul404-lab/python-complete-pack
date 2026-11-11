import json
from pathlib import Path

student = {"name": "Alice", "age": 25}
encoded = json.dumps(student, indent=2)
print(encoded)

# Demonstrate decoding without leaving a data file behind.
parsed = json.loads(encoded)
print(parsed["name"])

# Example file persistence (uncomment to write a file):
# Path("student.json").write_text(encoded, encoding="utf-8")
