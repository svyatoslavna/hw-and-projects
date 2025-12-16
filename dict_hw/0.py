""" Задача 0, слайд 16.
В файле data.json находится исходный словарь.
В файле data_new.json записаны результаты работы программы."""

import json

# 1: прочитать json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2: итерировать по ключам верхнего уровня, вывести их
    print("STRUCTURE (keys):")
    for key in data.keys():
        print(key)
    print("\n")

# 3: итерировать по значениям departments
    people = []
    for employees in data["departments"].values():
        people.extend(employees)
    print(*people, sep=", ", end=" work for us.\n")

# 4: итерировать по парам ключ-значение в departments
    for department, employees in data["departments"].items():
        print(f"{department.title()}: ", end="")
        print(*employees, sep=", ")

# 5: добавить нового сотрудника "David" в отдел "dev"
    data["departments"]["dev"].append("David")
    print("\nDavid is our new employee now!")
    
# 6: увеличить бюджет на 10%
    data["budget"] = int(data["budget"] * 1.1)
    print("\nOur budget is higher now!")

# демонстрирую все изменения через вывод:
    print(f"\nCURRENT FULL STRUCTURE (keys + values):\n{data}")

# 7: записать новый словарь обратно в файл
# но я всё-таки решила запистать его в новый файл,
# чтоб не потерять старые данные:
with open("data_new.json", "w", encoding="utf-8") as f:
     json.dump(data, f, ensure_ascii=False, indent=2)
print("\nДанные успешно сохранены в файл 'data_new.json'")
        
