correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3

while not logged_in and attempts < 3:

    password = input("Введите пароль: ")

    if password == correct_password:
        logged_in = True
        print("Доступ разрешен")
    else:
        attempts += 1
        print("Пароль неверный")

if logged_in == False:
    print("Кончились попытки, доступ запрещен")
