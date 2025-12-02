sales = [
    {"name": "Алексей", "sales": 150, "returns": 10},
    {"name": "Ольга", "sales": 200, "returns": 5},
    {"name": "Дмитрий", "sales": 80, "returns": 25},
    {"name": "Елена", "sales": 300, "returns": 8},
]

top_managers = [
    info["name"]
    for info in sales
    if (info["sales"] - info["returns"] >= 150)
    and (info["returns"] / info["sales"] * 100 < 10)
]

print(top_managers)
