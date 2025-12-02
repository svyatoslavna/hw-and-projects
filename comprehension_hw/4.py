employees = [("Иван", 45), ("Мария", 92), ("Петр", 33), ("Анна", 67)]

performance = [
    "Отлично" if percent >= 90 
    else "Хорошо" if percent >= 60 
    else "Требует улучшения"
    for name, percent in employees
]

print(performance)
