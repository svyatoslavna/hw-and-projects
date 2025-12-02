password = str()

while len(password) < 8:
    
    password = input("Введите пароль: ")
    
    if len(password) >= 8:
        print("Пароль принят!")
        break

    else:
        print("Пароль слишком короткий. Попробуйте снова.")

