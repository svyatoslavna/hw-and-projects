"""Задача 1, слайды 17-18"""

config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"],
}

# 1: получение значение learning_rate xерез скобки и через get()
print(f"learning_rate, скобки: {config["learning_rate"]}")
print(f"learning_rate, .get(): {config.get("learning_rate")}")

# 2: добавление нового параметра early_stopping
config["early_stopping"] = True

# 3: изменение batch_size
config["batch_size"] = 64

# 4: выведение только тех параметров, значение которых - числа
print("\nПараметры с численными значениями:")
for key, value in config.items():
    if isinstance(value, (int, float)):
        print(f"{key}: {value}")

# 5: создание копии конфигурации для тестирование  с batch_size=8 и epochs=1
config_new = config.copy()
config_new["batch_size"] = 8
config_new["epochs"] = 1

# проверяю, что cохранилось в config и сonfig_new
print("\nconfig:\n", config)
print("\nconfig_new:\n", config_new)
