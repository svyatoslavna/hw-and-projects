"""
Моя программа остановится и не будет собирать данные дальше, 
даже если пользователь решит ввести 0 в череде других чисел.
Числа, введённые в той же строке ПОСЛЕ 0, НЕ учитываются.
Числа, введённые в той же строке ДО 0, учитываются.
Например, ввод: 9 12 20 0.5 -7 0 100 20 1.
Вывод будет таким: 12 20.
"""


message = ""
numbers = []
final_numbers = []

while 0 not in numbers:  # пока не появится 0

    message = input()
    numbers = message.split()

    # в numbers я пока что записываю и 0 тоже, чтобы смочь его отследить,
    # чтобы сработало "while 0 not in numbers":
    numbers = [
        int(number) for number in numbers if number.isnumeric() and int(number) % 2 == 0
    ]
    final_numbers.extend(numbers)  # добавляю всё из numbers в финальный список

    # мы добавили в финальный список и 0 (если он был), и чётные положительные,
    # введённые после него,
    # теперь надо удалить 0 и всё, что было введено после:
    if 0 in final_numbers:
        final_numbers = final_numbers[: final_numbers.index(0)]

print(final_numbers)
