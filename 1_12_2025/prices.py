products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]
final_income = []

for i in range(4):

    final_income.append(prices[i] * quantities[i])

    print(
        f"{products[i]} по цене {prices[i]} - "
        f"продано в количестве {quantities[i]}.\n"
        f"Выручка = {final_income[i]} рублей.\n"
    )


print(
    f"Товар с максимальной выручкой: "
    f"{products[final_income.index(max(final_income))]}\n"
    f"Максимальная выручка: {max(final_income)}"
)
