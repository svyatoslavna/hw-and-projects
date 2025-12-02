mixed_data = [
    1,
    "hello",
    3.14,
    [1, 2],
    42,
    "world",
    0,
    (5, 6),
    {"name": "John"},
    True,
    {7, 8, 9},
]

lists, tuples, sets, integers = [], [], [], []
float_nums, strings, boolean, dicts = [], [], [], []


for structure in mixed_data:
    if isinstance(structure, list):
        lists.append(structure)
    elif isinstance(structure, tuple):
        tuples.append(structure)
    elif isinstance(structure, set):
        sets.append(structure)
    elif isinstance(structure, bool):
        boolean.append(structure)
    elif isinstance(structure, int):
        integers.append(structure)
    elif isinstance(structure, str):
        strings.append(structure)
    elif isinstance(structure, float):
        float_nums.append(structure)
    elif isinstance(structure, dict):
        dicts.append(structure)

print(f"Списки: {lists}\n"
      f"Кортежи: {tuples}\n"
      f"Множества: {sets}\n"
      f"Целые числа: {integers}\n"
      f"Числа с плавающей точкой: {float_nums}\n"
      f"Строки: {strings}\n"
      f"Логические значения: {boolean}\n"
      f"Словари: {dicts}")
