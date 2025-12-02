email_set = set()
email = str()

while True:

    email = input("Введите email: ")

    if email == "":
        print(f"Все email-адреса: {sorted(list(email_set))}")
        break
    else:
        email_set.add(email)
