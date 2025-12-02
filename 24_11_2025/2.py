commands_tuple = ("start", "stop", "pause", "quit")

command = str()

while True:

    command = input("Введите команду: ").lower()

    if command == "quit":
        print("Выход из программы")
        break

    elif command in commands_tuple:
        print(f"Выполняю {command}")

    else:
        print("Неизвестная команда")
