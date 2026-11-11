integer_value = 10
float_value = 3.14
string_value = "Python"
boolean_value = True
list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
set_value = {1, 2, 3}
dict_value = {"name": "Alice", "age": 25}

for value in (integer_value, float_value, string_value, boolean_value,
              list_value, tuple_value, set_value, dict_value):
    print(f"{value!r}: {type(value).__name__}")
