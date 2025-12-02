shopping_list = []
command = int()
object = str()

while command != 4:

    command = int(
        input(
            "Выберите действие: "
            "1 - добавить товар; "
            "2 - удалить товар; "
            "3 - показать список; "
            "4 - выйти: "
        )
    )

    if command == 1:
        object = input("Что добавляем в список? ").lower()
        shopping_list.append(object)
        print(f"Добавили {object}!")

    elif command == 2:
        object = input("Что удаляем из списка? ").lower()

        if object not in shopping_list:
            print(f"{object.title()} не было списке. ")
        else:
            shopping_list.remove(object)
            print(f"Удалили {object}!")

    else:
        print(f"Ваш список на данный момент: {shopping_list}")
