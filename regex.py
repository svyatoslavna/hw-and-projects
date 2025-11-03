import re

# Задача 1: Найти все цены с валютами (руб, $, евро, ₽)
# Ожидаемый результат: ['100 руб', '$50', '75.50 евро', '200₽']

text = "Цены: 100 руб, $50, 75.50 евро, 200₽, 300"
print(re.findall(r"\$\d+\.?\d*|\d+\.?\d*(?:\sруб|\sевро|₽)", text), "\n")


# Задача 2: Удалить все HTML-теги, оставив только текст
# Ожидаемый результат: "Текст жирный и курсивный"

html = "<div>Текст <b>жирный</b> и <i>курсивный</i></div>"
print(re.sub(r"<.*?>", "", html), "\n")


# Задача 3: Найти все номера версий (числа с точками)
# Ожидаемый результат: ['3.9', '17.0.1', '18.15.0', '1.2.3.4']

text = "Версии: Python 3.9, Java 17.0.1, Node.js v18.15.0, проект v1.2.3.4"
print(re.findall(r"\d+(?:\.\d+)*", text), "\n")


# Задача 4:
# 1. Найти email и телефон
# 2. Найти номер заказа (#12345)
# 3. Найти цену (1,500.50 руб)
# 4. Найти версию заказа (v2.1.5)

complex_text = """
Клиент Иван Иванов (ivan@mail.com, +7-912-345-67-89) 
заказал товар #12345 за 1,500.50 руб. 
Статус: ВЫПОЛНЕНО. Версия заказа v2.1.5.
Сайт: https://store.com/order/12345
"""

email = "".join(re.findall(r"\w+@\w+\.\w+", complex_text))
phone = "".join(re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", complex_text))
order = "".join(re.findall(r"#\d+", complex_text))
price = "".join(re.findall(r"\d+(?:,\d+)*(?:\.\d+)?\sруб", complex_text))
version = "".join(re.findall(r"v\d+(?:\.\d+)*", complex_text))

print(
    f"Email: {email}\nPhone: {phone}\nOrder: {order}\n"
    f"Price: {price}\nVersion: {version}"
)
