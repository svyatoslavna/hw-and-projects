"""Задача 5, слайд 24.
В файле nlp_service_config.json находится исходный словарь.
В файле nlp_service_config_updated.json записаны результаты работы программы."""

import json

# 1: загружаем конфигурацию из JSON-файла
with open("nlp_service_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 2: добавляем новую модель для "summarization" с соответствующими параметрами
config["models"]["summarization"] = {
        "path": "/models/qwen-summarization",
        "max_input_length": 2000,
        "supported_languages": ["en", "fr", "ru"],
    }

# 3: увеличиваем rate_limit на 50%
config["rate_limit"] = int(config["rate_limit"] * 1.5)

# 4: добавляем русский язык ("ru") в поддерживаемые языки для модели sentiment
config["models"]["sentiment"]["supported_languages"].append("ru")

# 5: создаём отдельный словарь только с настройками сервера
server_settings = config["server"].copy()
print(f"SERVER SETTINGS: {server_settings}")

# 6: сохраняем обновленную конфигурацию в новый файл nlp_service_config_updated.json
with open("nlp_service_config_updated.json", "w", encoding="utf-8") as f:
     json.dump(config, f, ensure_ascii=False, indent=2)
print("\nКонфигурация успешно сохранена в файл 'nlp_service_config_updated.json'")