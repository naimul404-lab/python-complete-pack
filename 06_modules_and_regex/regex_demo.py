import re

text = "Contact test@example.com or hello@domain.org"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
print(re.findall(pattern, text))
